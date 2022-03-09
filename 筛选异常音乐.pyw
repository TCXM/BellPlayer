from distutils import filelist
import time
import os
import shutil
import pyttsx3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
pt = pyttsx3.init()
def 音乐时长(path):
    if ".mp3" in path:
        print(MP3(path).info.length)
        return MP3(path).info.length
    elif ".flac" in path:
        print(FLAC(path).info.length)
        return FLAC(path).info.length

fileList = os.listdir(r"D:\\FTP\\未放")

for i in fileList:
    try:
        MusicPath = "D:\\FTP\\未放\\" + i
        print(音乐时长(MusicPath))
    except:
        oldMusicPath = "D:\\FTP\\未放\\" + i
        newMusicPath = "D:\\FTP\\异常\\" + i
        shutil.move(oldMusicPath,newMusicPath)