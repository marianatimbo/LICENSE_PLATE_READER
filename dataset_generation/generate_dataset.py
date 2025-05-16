import os 
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps
from tqdm import tqdm

characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
font_path = "C:/Windows/Fonts/timesbd.ttf"

image_size = (28,28)
images_per_class = 100

output_dir = "char_dataset"
os.makedirs(output_dir, exist_ok=True)

for char in tqdm(characters, desc="Generating dataset"):
    char_dir = os.path.join(output_dir, char)
    os.makedirs(char_dir, exist_ok=True)

    font = ImageFont.truetype(font_path, size=22)
    for i in range(images_per_class):
        img = Image.new("L",( image_size[0]*2 ,image_size[1]*2),color=255)
        draw = ImageDraw.Draw(img)

        bbox = draw.textbbox((0, 0), char, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        max_x = image_size[0]*2 - w
        max_y = image_size[1]*2 - h
        x = random.randint(0, max(0, max_x))
        y = random.randint(0, max(0, max_y))
        draw.text((x, y), char, font=font, fill=0)

        angle = random.uniform(-15, 15)
        img = img.rotate(angle, expand=False, fillcolor=255)
        img = ImageOps.fit(img, image_size, centering=(0.5, 0.5))
    
        filename = f"{char}_{i:03d}.png"
        img_path = os.path.join(char_dir, filename)
        img.save(img_path)


