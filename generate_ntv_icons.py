import cv2
import numpy as np
import os

# Configuration
input_image_path = 'нтв-рус.png'
output_folder = 'icons'
shift_range = range(-1, 10)
qual_labels = ['sd', 'hd']

# Read original image
original_image = cv2.imread(input_image_path)

for quality in qual_labels:
    for shift in shift_range:
        # Create a copy of the original image
        image_copy = original_image.copy()
        text_label = f'{quality}_{shift}'

        # Define font, scale, and color
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255)  # White text
        thickness = 2

        # Add text to image
        cv2.putText(image_copy, text_label, (10, 50), font, font_scale, color, thickness)

        # Define output filename
        output_filename = f'ntv_{quality}_{shift}.png'
        output_path = os.path.join(output_folder, output_filename)

        # Save the new icon
        cv2.imwrite(output_path, image_copy)