#!/usr/bin/env python3
import os
from PIL import Image
PATH = "/home/student/images/"
files = os.listdir(PATH)
for image in files:
    im = Image.open(os.path.join(PATH, image))
    im.rotate(-90).resize((128,128)).convert("RGB").save(f"/opt/icons/{image}", "jpeg")