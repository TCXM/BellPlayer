from distutils import filelist
import time
import os
import shutil
import pyttsx3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
pt = pyttsx3.init()
def 音乐时长(path):
    if ".mp3" in path:
        print(MP3(path).info.length)
        return MP3(path).info.length
    elif ".flac" in path:
        print(FLAC(path).info.length)
        return FLAC(path).info.length
    elif ".ogg" in path:
        print(OggVorbis(path).info.length)
        return OggVorbis(path).info.length

fileList = os.listdir(r"D:\\FTP\\未放")
#网易云音乐(ncm)，QQ音乐(qmc、mflac、mgg)，酷狗音乐(kgm)，虾米音乐(xm)，酷我音乐(kwm)
for i in fileList:
    if ".mflac" in i or ".mgg" in i or ".qmc" in i or ".kgm" in i or ".xm" in i or ".kwm" in i or ".ncm" in i:
        oldMusicPath = "D:\\FTP\\未放\\" + i
        newMusicPath = "D:\\FTP\\异常\\" + i
        shutil.move(oldMusicPath,newMusicPath)
    try:
        MusicPath = "D:\\FTP\\未放\\" + i
        if  音乐时长(MusicPath) == None:
            oldMusicPath = "D:\\FTP\\未放\\" + i
            newMusicPath = "D:\\FTP\\异常\\" + i
            shutil.move(oldMusicPath,newMusicPath)
    except:
        oldMusicPath = "D:\\FTP\\未放\\" + i
        newMusicPath = "D:\\FTP\\异常\\" + i
        shutil.move(oldMusicPath,newMusicPath)