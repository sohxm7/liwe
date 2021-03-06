import os
from PIL import Image
from screeninfo import get_monitors

path = os.getcwd()

for m in get_monitors():
    wid = str(m).split()[2][-5:-1]
    hei = str(m).split()[3][-5:-1]

print("wait a sec...")

wid = int(wid)
hei = int(hei)

size = wid, wid

print("")

for i in range(1, 9):
    print("Scaling [",i,"/ 8 ]")
    for j in ["b","c","d","l"]:
        im = Image.open(path+"/images/"+j+str(i)+".jpg")
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(path+"/images/new/"+j+str(i)+".png", "PNG")

print("")

x = int((wid-hei)/2)
for i in range(1, 9):
    print("Cropping [",i,"/ 8 ]")
    for j in ["b","c","d","l"]:
        im = Image.open(path+"/images/new/"+j+str(i)+".png")
        im_resized = im.crop((0, x, wid, x+hei))
        im_resized.save(path+"/images/new/"+j+str(i)+".png", "PNG")

print("\nDone Successfully...")
