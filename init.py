from PIL import Image
from screeninfo import get_monitors
for m in get_monitors():
    wid = str(m).split()[2][-5:-1]
    hei = str(m).split()[3][-5:-1]

print("Starting Screen Size Optimizations...")
wid = int(wid)
hei = int(hei)
size = wid, hei
for i in range(1, 9):
    print(i)
    for j in ["b","c","d","l"]:
        im = Image.open("images/"+j+str(i)+".jpg")
        im_resized = im.resize(size, Image.ANTIALIAS)
        im_resized.save("images/"+j+str(i)+".png", "PNG")
print("Done Successfully...")
