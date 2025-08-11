import os
from PIL import Image

# Input and output folders
input_folder = 'images'
output_folder = 'resized'
new_size = (800, 600)  # width x height

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize and save images
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        img_resized = img.resize(new_size)
        
        save_path = os.path.join(output_folder, filename)
        img_resized.save(save_path)

print("All images resized and saved to 'resized/' folder.")