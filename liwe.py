#!/usr/bin/env python

import os
from PIL import Image
from datetime import datetime

dixt = {"cliff": "/home/soham/liwe/images/c",
        "beach": "/home/soham/liwe/images/b",
        "desert":"/home/soham/liwe/images/d",
        "lake":  "/home/soham/liwe/images/l"
        }

# For selecting the wallpaper edit line below
# wallpapers: "cliff", "beach", "desert", "lake"
selected = dixt["cliff"]

# Take current Time
nowx = datetime.now()
hour = int(nowx.strftime("%H"))
minx = int(nowx.strftime("%M"))

# Divide 24 hours into 8 equal parts
# Determine the alpha of next image
imgx = int(hour/3) + 1
alpx = (((hour%3)*60)+minx)/180
if imgx==8:
        nexx = 1
else:
        nexx = imgx + 1

# Merge both images based on time and alpha
bg = Image.open(selected+str(imgx)+".png")
fg = Image.open(selected+str(nexx)+".png")
Image.blend(bg, fg, alpx).save("out.png")

# Command for changing the wallpaper
# Can customise it accordingly
command = "feh --bg-scale out.png"
os.system(command)
