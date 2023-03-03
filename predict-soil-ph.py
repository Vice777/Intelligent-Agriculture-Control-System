import cv2
import numpy as np

# Load image and convert to HSV
img = cv2.imread('soil.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define range of green color in HSV
lower_green = np.array([35, 20, 20])
upper_green = np.array([85, 255, 255])

# Threshold the HSV image to get only green colors
mask = cv2.inRange(hsv, lower_green, upper_green)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)

# Convert to grayscale and apply Gaussian blur
gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)

# Apply adaptive thresholding
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,            cv2.THRESH_BINARY,11,2)

# Find contours and draw them on the original image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)

def compute_pH_value(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale image
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Binarize the image using Otsu's thresholding method
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Compute the white pixel percentage
    white_pixel_percent = np.sum(binary == 255) / np.size(binary) * 100

    # Calculate the pH value using the white pixel percentage and a pre-defined calibration curve
    pH_value = 4.5 + 1.5 * (white_pixel_percent - 8) / (64 - 8)

    return pH_value


# Compute average pH value of the soil
pH_values = []
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)
    crop = thresh[y:y+h, x:x+w]
    pH_value = compute_pH_value(img[y:y+h, x:x+w])
    pH_values.append(pH_value)
average_pH = sum(pH_values) / len(pH_values)
print("Average pH value:", average_pH)

# Show the final result
cv2.imshow('result',img)
cv2.waitKey(0)
cv2.destroyAllWindows()






