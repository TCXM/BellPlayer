import time
import os
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random
import shutil
import pyttsx3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.ogg import OggFileType
pt = pyttsx3.init()
m=PyMouse()
k=PyKeyboard()
def 音乐时长(path):
    if ".mp3" in path:
        print(MP3(path).info.length)
        return MP3(path).info.length
    elif ".flac" in path:
        print(FLAC(path).info.length)
        return FLAC(path).info.length
    elif ".ogg" in path:
        print(OggFileType(path).info.length)
        return OggFileType(path).info.length
def 播放音乐():
    fileList = os.listdir(r"D:\\FTP\\未放")
    listLenth = len(fileList)
    n = random.randint(0,listLenth)
    print(n)
    musicPath = fileList[n]
    oldMusicPath = "D:\\FTP\\未放\\" + musicPath
    newMusicPath = "D:\\FTP\\已放\\" + musicPath
    shutil.move(oldMusicPath,newMusicPath)
    pt.say("即将播放")
    pt.say(musicPath)
    pt.runAndWait()
    os.startfile(newMusicPath)
    time.sleep(音乐时长(newMusicPath))
播放音乐()