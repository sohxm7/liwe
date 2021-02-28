## Liwe - under work

Liwe is a live wallpaper changer written in python. Tho it only support 1 monitor setup as of now.

### Dependencies
+ [feh](https://github.com/derf/feh)
+ [screeninfo](https://pypi.org/project/screeninfo/)

### Installation and configuration
```
git clone https://github.com/sohxm7/liwe.git
cd liwe
python init.py 
chmod +x liwe.py
```
### Important
Edit lines 7 to 10 in liwe.py and replace ```<soham>``` with ```<your user name>```

### Add in i3 config
```
exec_always --no-startup-id "python $HOME/liwe/liwe.py"
exec_always --no-startup-id "while sleep 10m; do python $HOME/liwe/liwe.py; done"
# Exit i3 and login again
```
images were taken from [sunpaper](https://github.com/hexive/sunpaper).
