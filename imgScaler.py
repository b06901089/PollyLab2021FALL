### Resize images into certain size
### Move & Rename images into another folder having names like 1.jpg 2.jpg 3.jpg

from PIL import Image, ImageFile
import os, sys

ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "./temple/"
output_path = "./temple_resized/"

starting_idx = 2976
dirs = os.listdir(path)

def resize():
    if os.path.isdir(output_path) == False:
        os.makedirs(output_path)

    for idx, item in enumerate(dirs):
        if not item.startswith('.'):
            if os.path.isfile(path + item):
                im = Image.open(path + item)
                imResize = im.resize((800, 800), Image.ANTIALIAS)
                imResize.save(output_path + str(idx+starting_idx) + '.jpg', 'JPEG', quality=90)

resize()