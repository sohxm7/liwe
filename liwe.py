from PIL import Image
import os
from datetime import datetime

dixt = {"cliff":"images/The-Cliffs/",
        "beach":"images/The-Beach/",
        "desert":"images/The-Desert/",
        "lake":"images/The-Lake/"
        }
selected = dixt["cliff"]

nowx = datetime.now()
hour = int(nowx.strftime("%H"))
minx = int(nowx.strftime("%M"))

imgx = int(hour/3) + 1
alpx = (((hour%3)*60)+minx)/180

if imgx==8:
        nexx=0
else:
        nexx = imgx + 1
        
bg = Image.open(selected+str(imgx)+".jpg")
fg = Image.open(selected+str(nexx)+".jpg")
Image.blend(bg, fg, alpx).save("out.png")

command = "feh --bg-scale out.png"
os.system(command)
