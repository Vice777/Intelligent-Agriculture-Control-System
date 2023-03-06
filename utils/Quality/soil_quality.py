import cv2
import numpy as np


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

# Define the lower and upper bounds of the color range for each pH value
lower_bounds = [(0, 0, 190), (0, 0, 140), (100, 70, 30), (35, 90, 0)]
upper_bounds = [(5, 255, 255), (10, 255, 255), (120, 255, 255), (90, 255, 255)]
pH_values = [4.5, 6.0, 7.5, 9.0]


def get_pH(image):
    # Convert the image to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Find the color range that the test paper falls within
    for i in range(len(lower_bounds)):
        lower_bound = np.array(lower_bounds[i])
        upper_bound = np.array(upper_bounds[i])
        mask = cv2.inRange(hsv_image, lower_bound, upper_bound)
        if cv2.countNonZero(mask) > 0:
            return pH_values[i]

    # If the test paper color is not within any of the defined ranges, return None
    return None

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

# Load the input image
image = cv2.imread("red.jpg")

# Extract the pH value and RGB values from the image
pH_value = get_pH(image)
R, G, B = get_RGB(image)
soil_color=get_soil_color(image)

# Determine the quality of the soil based on the pH value and RGB values
soil_quality = determine_soil_quality(pH_value, R, G, B)

# Color
print(f"The color of the soil is {soil_color}")

#pH value
print(f"The ph Value of the soil is {pH_value}")

# Print the predicted soil quality
print("Predicted soil quality: " + soil_quality)