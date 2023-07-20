from PIL import Image
import os

def resize_without_interpolation(image_path, new_width, new_height):
    # Open the image
    image = Image.open(image_path)

    # Resize the image without interpolation (nearest-neighbor resizing)
    resized_image = image.resize((new_width, new_height), Image.NEAREST)

    return resized_image

if __name__ == "__main__":
    # Example usage:
    input_folder = "path/to/input/folder"
    output_folder = "path/to/output/folder"
    new_width = 200
    new_height = 150

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

    # Resize and save each image
    for image_file in image_files:
        input_image_path = os.path.join(input_folder, image_file)
        output_image_path = os.path.join(output_folder, image_file)

        resized_image = resize_without_interpolation(input_image_path, new_width, new_height)
        resized_image.save(output_image_path)
        print(f"Image '{image_file}' resized without interpolation and saved.")
