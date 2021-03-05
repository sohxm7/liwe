#!/usr/bin/env python

import os
from PIL import Image
from datetime import datetime

dixt = {"cliff": "/home/soham/liwe/images/new/c",
        "beach": "/home/soham/liwe/images/new/b",
        "desert":"/home/soham/liwe/images/new/d",
        "lake":  "/home/soham/liwe/images/new/l"
        }

# For selecting the wallpaper edit line below
# wallpapers: "cliff", "beach", "desert", "lake"
selected = dixt["beach"]

# Take current Time
nowx = datetime.now()
hour = int(nowx.strftime("%H"))
minx = int(nowx.strftime("%M"))

if hour < 4:
        imgx = 1
        nexx = 1
        alpx = 0
elif hour < 5:
        imgx = 1
        nexx = 2
        alpx = minx/60
elif hour < 7:
        imgx = 2
        nexx = 3
        alpx = ((hour-4)+minx)/120
elif hour < 9:
        imgx = 3
        nexx = 4
        alpx = ((hour-6)+minx)/120
elif hour < 11:
        imgx = 4
        nexx = 5
        alpx = ((hour-8)+minx)/120
elif hour < 13:
        imgx = 5
        nexx = 6
        alpx = ((hour-10)+minx)/180
elif hour < 16:
        imgx = 6
        nexx = 7
        alpx = ((hour-12)+minx)/180
elif hour < 20:
        imgx = 7
        nexx = 8
        alpx = ((hour-15)+minx)/240
else:
        imgx = 8
        nexx = 1
        alpx = ((hour-19)+minx)/240

# Merge both images based on time and alpha
bg = Image.open(selected+str(imgx)+".png")
fg = Image.open(selected+str(nexx)+".png")
Image.blend(bg, fg, alpx).save("out.png")

# Command for changing the wallpaper
# Can customise it accordingly
command = "feh --bg-scale out.png"
os.system(command)
