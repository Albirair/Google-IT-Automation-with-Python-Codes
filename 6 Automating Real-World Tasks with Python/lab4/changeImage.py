#!/usr/bin/env python3
import os
from PIL import Image
PATH = "/home/student/supplier-data/images/"
files = os.listdir(PATH)
for image in files:
    if image[-5:] == ".tiff":
        joinedPath = os.path.join(PATH, image)
        im = Image.open(joinedPath)
        im.resize((600, 400)).convert("RGB").save(
            joinedPath[:-4] + "jpeg", "jpeg")