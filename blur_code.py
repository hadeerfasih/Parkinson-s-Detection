import cv2
import os

def apply_blur(image):
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
    return blurred_image

# Define the path to the folder containing the original images
folder_path = r'C:\Users\pc\Downloads\CDSS_FINAL_PROJECT\spiral_tg_thin\training\healthy'

# Iterate over the original images in the folder
for filename in os.listdir(folder_path):
    # Check if the file is an image (you can adjust the valid image extensions if needed)
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read the original image
        image_path = os.path.join(folder_path, filename)
        image = cv2.imread(image_path)

        # Apply blur
        blurred_image = apply_blur(image)

        # Save the augmented image
        augmented_image_path = os.path.join(folder_path, 'blurred_' + filename)
        cv2.imwrite(augmented_image_path, blurred_image)