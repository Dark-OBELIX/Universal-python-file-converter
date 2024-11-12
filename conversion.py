from PIL import Image
import os

def convert_image(input_file, output_file):
    try:
        # Open the source image
        with Image.open(input_file) as img:
            # Convert the image to RGB mode (required for JPG files)
            rgb_image = img.convert('RGB')
            # Save the image in the target format
            rgb_image.save(output_file)
        print(f'Successful conversion: {input_file} -> {output_file}')
        return True
    except Exception as e:
        print(f'Conversion error: {e}')
        return False
