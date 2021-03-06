import os
from PIL import Image
from screeninfo import get_monitors

path = os.getcwd()

for m in get_monitors():
    wid = str(m).split()[2][-5:-1]
    hei = str(m).split()[3][-5:-1]

print("\nThis will take about 90 seconds. Don't worry, you have to go through this only once\n")

wid = int(wid)
hei = int(hei)

size = wid, wid

print("")

for i in range(1, 9):
    print("Scaling [",i,"/ 8 ]")
    for j in ["b","c","d","l"]:
        im = Image.open(path+"/liwe/images/"+j+str(i)+".jpg")
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save(path+"/liwe/images/new/"+j+str(i)+".png", "PNG")

print("\n")

x = int((wid-hei)/2)
for i in range(1, 9):
    print("Cropping [",i,"/ 8 ]")
    for j in ["b","c","d","l"]:
        im = Image.open(path+"/liwe/images/new/"+j+str(i)+".png")
        im_resized = im.crop((0, x, wid, x+hei))
        im_resized.save(path+"/liwe/images/new/"+j+str(i)+".png", "PNG")

print("\nDone Successfully...")
