import time
import os
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random
import shutil
import pyttsx3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis
pt = pyttsx3.init()
m=PyMouse()
k=PyKeyboard()
time.sleep(1)
#k.press_keys([k.alt_l_key,k.space_key,"n"])
t = 0
a = 0
normal = True

def 点击麦克风():
    m.click(30,794)
def 播放上课铃():
    点击麦克风()
    os.startfile("D:\\编程\\PythonProject\\铃声管理\\上课铃2.mp3")
    print("播放上课铃")
    time.sleep(13)
    点击麦克风() 
def 播放下课铃():
    点击麦克风()
    os.startfile("D:\\编程\\PythonProject\\铃声管理\\下课铃.mp3")
    print("播放下课铃")
    time.sleep(39)
    点击麦克风()
def 播放考试铃():
    点击麦克风()
    os.startfile("D:\\编程\\PythonProject\\铃声管理\\考试铃.m4a")
    print("播放考试铃")
    time.sleep(22)
    点击麦克风()
    time.sleep(60)
def 播放眼保健操():
    点击麦克风()
    os.startfile("D:\\编程\\PythonProject\\铃声管理\\眼保健操.mp3")
    print("播放眼保健操")
    time.sleep(345)
    点击麦克风()
def 音乐时长(path):
    if ".mp3" in path:
        return MP3(path).info.length
    elif ".flac" in path:
        return FLAC(path).info.length
    elif ".ogg" in path:
        return OggVorbis(path).info.length  
def 播放音乐():
    global a
    os.startfile("D:\\编程\\PythonProject\\铃声管理\\筛选异常音乐.pyw")
    time.sleep(0.1)
    try:
        musicPath = "压根没抽出来"
        fileList = os.listdir(r"D:\\FTP\\未放")
        listLenth = len(fileList)
        n = random.randint(0,listLenth)
        musicPath = fileList[n]
        print(musicPath)
        oldMusicPath = "D:\\FTP\\未放\\" + musicPath
        newMusicPath = "D:\\FTP\\已放\\" + musicPath
        wrongMusicPath = "D:\\FTP\\异常\\" + musicPath
        shutil.move(oldMusicPath,newMusicPath)
        print("文件移动完成")
        pt.say("即将播放")
        pt.say(musicPath)
        pt.runAndWait()
        try:
            a = 音乐时长(newMusicPath)
            print("单曲时长 =",a)
            os.startfile(newMusicPath)
            print("开始播放")
            time.sleep(音乐时长(newMusicPath))
        except:
            print("音乐播放异常:",musicPath)
            pt.say("音乐播放异常")
            pt.say(musicPath)
            pt.runAndWait
            shutil.move(newMusicPath,wrongMusicPath)
            a = 0
    except:
        print("音乐抽取异常:",musicPath)
        pt.say("音乐抽取异常")
        pt.say(musicPath)
        pt.runAndWait
        a = 0


while 1:
    t = int(time.strftime("%H%M"))
    d = int(time.strftime("%w"))
    print(t)
    if normal == True:
        if ((t == 715 or t == 805 or t == 855) and d!=1)or((t==710 or t ==800 or t == 850)and d == 1) or t == 1000 or t == 1055 or t == 1145 or t == 1420 or t == 1510 or t == 1615 or t == 1710 or t == 1930 or t == 2030 or t == 2140:
            播放下课铃()
            time.sleep(60)
        if (t == 858  and d != 1)or (t==853 and d == 1) or t == 1513:
            点击麦克风()
            x=1
            T=0
            while T < 900:
                print("准备播放第",x,"首歌")
                x+=1
                播放音乐()
                T += a
                print("已经播放 =",T)
            点击麦克风()
        if t == 1330 :
            点击麦克风()
            播放下课铃()
            time.sleep(1)
            点击麦克风()
            播放音乐()
            播放音乐()
            点击麦克风()
                
        if ((t == 645 or t == 725 or t == 815) and d!=1)or((t==645 or t ==720 or t == 810)and d == 1) or t == 920 or t == 1105 or t == 1215 or t == 1340 or t == 1430 or t == 1535 :
            播放上课铃()
            time.sleep(60) 
        if t == 1010 or t == 1625:
            播放上课铃()
            time.sleep(1)
            播放眼保健操()
    else:
        if t == 1800 or t == 2020 or t == 1405 or t == 1520:
            播放考试铃()
        if t == 2000 or t == 2135:
            播放考试铃()
    time.sleep(10)
