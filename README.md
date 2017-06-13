VLC Scrobbler for myshows.me
===================================
Myshowsscrobbler allows you to scrobble watched series to [myshows.me](myshows.me)</br>
It does its best trying to figure out season and series numbers of shows you're watching</br>
It's still in early development and might be unstable


Requirements
------------

python 3.3+

Installation
-----
```
git clone https://github.com/Elcaten/myshowsscrobbler
cd myshowscrobbler
python setup.py install
```

VLC settings: 
-----
+ **Preferences -> Tools**
+ Then check **All** option in bottom left
+ Go to **Interface -> Main interfaces**
+ Check **Web** option
+ Go to **Interface -> Main interfaces -> Lua**
+ Set password
+ Open config.py and change VLC_PASSWORD accordingly


Usage
-----

```
python -m myshowscrobbler
```


