#!/usr/bin/env python3

from os import listdir
from PIL import Image

# Open folder with images
source_dir = "images/"
folder = [f for f in listdir(source_dir) if f.startswith("ic_")]

# transform images and save with same name
for image in folder:
    im = Image.open(source_dir + image)
    new_im = im.rotate(90).resize((128,128))
    new_im = new_im.convert("RGB")
    new_im.save('/opt/icons/{}.jpeg'.format(image))

