## Liwe - under work

taken from github.com/hexive/sunpaper which was written in bash, but wasnt working on my machine for some reason. 

Liwe is written in python (and kinda slow) but does the work perfectly, also smooth fading between wallpapers is added.

### Dependencies
+ [feh](https://github.com/derf/feh)
+ [screeninfo](https://pypi.org/project/screeninfo/)

### Installation and configuration
```
git clone https://github.com/sohxm7/liwe.git
cd liwe
python init.py 
```
### Add in i3 config
```
exec_always --no-startup-id "python $HOME/liwe/liwe.py"
exec_always --no-startup-id "while sleep 10m; do python $HOME/liwe/liwe.py; done"
```
