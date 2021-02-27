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

bg = Image.open(selected+str(imgx-1)+".jpg")
fg = Image.open(selected+str(imgx)+".jpg")
Image.blend(bg, fg, alpx).save("out.png")
comandx = "feh --bg-scale out.png"
os.system(comandx)
