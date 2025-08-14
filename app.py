import os
from PIL import Image

# Input and output folders
input_folder = "images"       # folder containing original images
output_folder = "resized"     # folder to save resized images
new_size = (800, 800)         # desired size


os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
        img_path = os.path.join(input_folder, filename)
        
        try:
            img = Image.open(img_path)
            img_resized = img.resize(new_size)

            # Convert to RGB if needed (fix RGBA/WEBP transparency issue)
            if img_resized.mode in ("RGBA", "P"):
                img_resized = img_resized.convert("RGB")

            
            output_name = os.path.splitext(filename)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_name)
            img_resized.save(output_path, "JPEG")

            print(f" Resized and saved: {output_path}")
        
        except Exception as e:
            print(f" Failed for {filename}: {e}")

print("🎯 All images processed!")
