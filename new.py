import cv2
import numpy as np
import os

# For soil type(color)
lower_bounds_color = [(0, 0, 0), (0, 0, 100), (0, 110, 120), (0, 100, 0), (20, 110, 160)]
upper_bounds_color = [(60, 60, 60), (50, 50, 180), (50, 255, 255), (80, 180, 120), (60, 255, 255)]
soil_types = ['Black', 'Cinder', 'Laterite', 'Peat', 'Yellow']


def get_soil_color(image):
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Find the color range that the soil color falls within
    for i in range(len(lower_bounds_color)):
        lower_bound = np.array(lower_bounds_color[i])
        upper_bound = np.array(upper_bounds_color[i])
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        if cv2.countNonZero(mask) > 0:
            return soil_types[i]

    # If the soil color is not within any of the defined ranges, return None
    return None


def get_pH(img):
    # Load the image and convert it to HSV color space
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the color range for soil in HSV color space
    lower_range = np.array([0, 0, 0])
    upper_range = np.array([179, 255, 150])

    # Create a binary mask for soil pixels
    mask = cv2.inRange(hsv_img, lower_range, upper_range)

    # Apply morphology operations to remove noise and fill gaps in the mask
    kernel = np.ones((5, 5), np.uint8)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=2)

    # Find the contours of the soil regions
    contours, hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Calculate the average color values of the soil regions
    hue_sum = saturation_sum = value_sum = count = 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        roi = hsv_img[y:y + h, x:x + w]
        hue_sum += np.sum(roi[:, :, 0])
        saturation_sum += np.sum(roi[:, :, 1])
        value_sum += np.sum(roi[:, :, 2])
        count += roi.shape[0] * roi.shape[1]

    # Calculate the average color values of the soil regions
    hue_avg = hue_sum / count
    saturation_avg = saturation_sum / count
    value_avg = value_sum / count

    # Calculate the pH value based on the average color values
    ph_value = 6.5 - ((hue_avg - 10) / 23)

    return ph_value


def get_RGB(image):
    # Extract the RGB values from the image
    R, G, B = cv2.split(image)
    R = cv2.mean(R)[0]
    G = cv2.mean(G)[0]
    B = cv2.mean(B)[0]
    return R, G, B


def determine_soil_quality(pH_value, R, G, B):
    # Check if pH value is within acceptable range
    if pH_value is None or pH_value < 6.0 or pH_value > 8.0:
        return "Poor"

    # Calculate the average RGB value of the image
    avg_RGB = (R + G + B) / 3.0

    # Check if the average RGB value is within acceptable range
    if avg_RGB < 100:
        return "Poor"
    elif avg_RGB < 150:
        return "Fair"
    else:
        return "Good"


def quality(im):
    # Load the input image
    image = cv2.imread(im)

    # Extract the pH value and RGB values from the image
    pH_value = get_pH(image)
    if pH_value < 5.5:
        soil_type = "Strongly acidic soil"
    elif pH_value < 6.5:
        soil_type = "Acidic soil"
    elif pH_value < 7.5:
        soil_type = "Neutral soil"
    elif pH_value < 8.5:
        soil_type = "Alkaline soil"
    else:
        soil_type = "Strongly alkaline soil"

    R, G, B = get_RGB(image)
    soil_color = get_soil_color(image)

    # Determine the quality of the soil based on the pH value and RGB values
    soil_quality = determine_soil_quality(pH_value, R, G, B)

    # Color
    #print(f"The color of the soil is {soil_color}")

    # # pH value
    #print(f"The ph Value of the soil is {pH_value}")

    # # Soil Type
    #print(f"The type of the soil is {soil_type}")

    # # Print the predicted soil quality
    #print("Predicted soil quality: " + soil_quality)

    dic = {
        "soil_color": soil_color,
        "pH_value": pH_value,
        "soil_type": soil_type,
        "soil_quality": soil_quality
    }
    return dic
