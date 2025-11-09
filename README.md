Setup Stage
---
python version requirement: 3.8.5 (64 bits)<br>
!!! tensorFlow needs python 64 bits !!!<br>
upgrade your pip to get the correct version of spleeter<br>

```
python -m pip install --upgrade pip
```

check your python version first:
```
python --version
```
should say 3.8.5

(in VS code, press Ctrl+Shift+P, type in Python:select interpreter, selcet the correct python version, restart VS code, if still doesn't work, put the path to python 3.8.5 to the top of the PATH in both USER and System)

set up a virtual environment

```
python -m venv audioAgent
```

activate the venv
```
.\audioAgent\Scripts\activate
```
you command line should start with (audioAgent)

install the package from requirement
```
pip install -r .\requirements.txt
```

check your spleeter version
```
spleeter --version
```
should say : Spleeter Version: 2.4.0

install ffmpeg

<a>https://www.ffmpeg.org/download.html</a>
add the path to "bin" folder to path

check your ffmpeg version
```
ffmpeg
```

this should print out some information and the -h option

finally, check if the command 'spleeter' works

```
spleeter separate <path to mp3 file> -p spleeter:4stems -o <output path>
```
you are now done with the Setup Stage
---