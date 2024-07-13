from PIL import Image
from io import BytesIO

def calc_font_size(text):
    words = text.split()
    print('words count:', len(words))
    if len(words) < 20:
        return 50
    elif len(words) < 30:
        return 40
    elif len(words) < 40:
        return 30
    elif len(words) < 50:
        return 27
    elif len(words) < 60:
        return 25
    else:
        return 22

def resize_image(image_path, max_size=10 * 1024 * 1024):
    with Image.open(image_path) as img:
        while True:
            img_byte_arr = BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_size = img_byte_arr.tell()

            if img_size <= max_size:
                img_byte_arr.seek(0)
                return img_byte_arr

            img = img.resize((int(img.width * 0.9), int(img.height * 0.9)))
