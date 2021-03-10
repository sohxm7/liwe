## Liwe 

Liwe is a live wallpaper written in python. Supports only 1 monitor setup as of now.

![wallpaper](images/liwe.gif)

### Dependencies
+ [xwallpaper](https://archlinux.org/packages/community/x86_64/xwallpaper/)
+ [screeninfo](https://pypi.org/project/screeninfo/)

### Install and Config
```
git clone https://github.com/sohxm7/liwe.git
cd liwe
python init.py 
chmod +x liwe.py
```

### Add in ```.config/i3/config```
```
exec_always --no-startup-id "xwallpaper --center $HOME/liwe/out.png"
exec_always --no-startup-id "python $HOME/liwe/liwe.py"
exec_always --no-startup-id "while sleep 10m; do python $HOME/liwe/liwe.py; done"
# Exit i3 and login again
```
### Changing wallpaper
Edit line 15 of liwe.py with desired wallpaper name.
Available Wallpapers: "cliff", "beach", "desert", "lake"

```selected = dixt["beach"]```



images were taken from [sunpaper](https://github.com/hexive/sunpaper).
