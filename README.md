# 铃声播放程序v1.0使用手册

### 前言

Hi你好，省太高的优秀同学，打开这份手册的你一定很懂电脑欸，必然能胜任播放铃声和音乐这项工作。

### 实现功能

本程序将实现定时播放上课铃、下课铃以及定时开始播放音乐等功能。

### 工作原理

本程序依赖python运行，通过点击你的腾讯会议的麦克风按钮打开你的麦克风（有社死风险，请小心使用），然后播放音乐，等音乐结束后再点击麦克风按钮关闭你的麦克风。

* 关于麦克风点击

  * 麦克风通过模拟鼠标的方式进行点击，需要手动更改鼠标点击的位置
* 关于铃声播放

  * TimeTable文件是一个文本文件，可以用记事本打开，程序将从中读取定时播放铃声的时间表，按照时间播放铃声。
* 关于音乐播放

  * 音乐分为15分钟音乐播放和单首音乐播放，音乐播放将从“未放”文件夹抽取一首歌放到“已放”文件夹并播放该歌曲，如果遇到**加密格式**音乐或者文件属性有问题则放入“异常”文件夹。你只要向“未放”文件夹里面丢歌曲就可以了。
  * 加密格式有：网易云音乐(ncm)，QQ音乐(qmc、mflac、mgg)，酷狗音乐(kgm)，虾米音乐(xm)，酷我音乐(kwm)等等，可以通过一些解密网站解密。
  * 15分钟音乐：指的是连续播放15分钟的音乐，一般在5首音乐左右，根据音乐时长判断，如果一首歌放完后总计已经放满15分钟，则停止播放，如果没有满15分钟则再抽取一首播放，所以15分钟音乐播放不是准确的播放15分钟，会因为音乐长度有所延后，请预留出缓冲时间以免被老师怼。
  * 单首音乐：指的是到达指定的时间抽取一首歌出来播放。
* 关于程序运行过程

  * 程序运行过程中会每隔10秒判断一次是否到达指定的时间，会有一个黑色的窗口打印出运行信息。
* 关于模式1和模式2

  * 模式一是正常模式，运行TimeTable的1-8行，播放上课铃、下课铃和音乐；模式二是考试模式，运行TimeTable的1、2、9行，播放考试铃。

### 使用方法 #重要#

* 第一步：修改鼠标点击麦克风按钮的坐标

  * 双击运行“显示鼠标坐标.exe”，每隔一秒它会显示出一个鼠标当前的坐标，一共显示十次，你要做的就是打开它然后在十秒内切换到腾讯会议，把光标放在麦克风按钮上，等10秒以后再回到程序运行界面，记下最后一个坐标，按照 xxx  xxx 的格式（数字+空格+数字）填入TimeTable第二行（如图）。
  * ![image.png](assets/image-20220411131112-mcifuws.png)![image.png](assets/image-20220411131204-39qxbzv.png)
  * #注意#这个坐标是相对你的显示屏的坐标，如果你改动腾讯会议的窗口则这个坐标核能点不到你的麦克风。所以，建议==将腾讯会议全屏==（如图）并在设置中选择“==始终显示工具栏==”![image.png](assets/image-20220411131600-zytj79l.png)

    ![image.png](assets/image-20220411131810-lxyf44a.png)
* 第二步：核对/修改时间表

  * 在TimeTable文件中一共有9行内容  #注意#==不要在TimeTable里输入任何数字以外的内容==

    ![image.png](assets/image-20220411132108-beawm8l.png)
  * 第一行：模式选择，模式1为正常模式，模式2 为考试模式。#注意#详见上文“工作原理”。
  * 第二行：鼠标点击的坐标，前面已经讲过
  * 第三行：周一==上课铃==播放时间
  * 第四行：除周一以外的==上课铃==播放时间
  * 第五行：周一==下课铃==播放时间
  * 第六行：除周一以外的==下课铃==播放时间
  * 第七行：15分钟音乐播放开始时间#注意#详见上文“工作原理”。
  * 第八行：单首音乐播放时间
  * 第九行：考试铃声播放时间。#注意#目前考试铃声只有一个，所以开始和结束放的是同一个铃声。
  * #注意#时间格式为XXXX，例如 <u>17：10</u> 在TimeTable中应写为 <u>1710</u> 。相邻时间之间加入一个**空格**
  * #注意#==如果不需要某一行，例如不需要播放单首音乐那一行，请将那一行改为“0”而不是将一整行留空（如图），换句话说，一行里的时间你可以随意删掉一个时间，但不能删干净，起码留个0，不能被识别为空行，会报错的。==

    ![image.png](assets/image-20220411135422-38k56ff.png)
* 第三步：运行程序

  * 双击运行“BellPlayer.exe”即程序启动。
  * #注意#程序运行过程中可以更改TimeTable内的内容，但需要保存后关闭TimeTable并重新启动“BellPlayer.exe”，否则不会生效。
  * 开始运行后你就好好上课去吧，让它运行着就行，运行窗口可以最小化。

### 拓展应用

如果你喜欢折腾，那你可以用自己的铃声音乐文件替换为你自己的，但文件名和格式必须完全一致，例如把你自己的音乐改名为“上课铃”，转格式为mp3，然后替换掉原来文件夹里的“上课铃.mp3”

你甚至可以像我一样搭建FTP服务器让同学们在家里也可以往“未放”文件夹投入他们喜欢的歌曲，具体方法自行百度，挺复杂的,前提是你家的路由器有公网ip地址。

### 什么？还有问题？

如果你还有问题，可以通过qq：3122759673联系我。

### 源代码

```python
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

def 点击麦克风():
    try:
        m.click(MousePlace[0],MousePlace[1])
    except:
        print("鼠标点击异常")
def PlayBell(name):
    try:
        os.startfile(name)
        time.sleep(音乐时长(name))
    except:
        print("未找到\"",name,"\"")
        time.sleep(100)
def 播放上课铃():
    点击麦克风()
    PlayBell("上课铃.mp3")
    print("播放上课铃")
    点击麦克风()
def 播放下课铃():
    点击麦克风()
    PlayBell("下课铃.mp3")
    print("播放下课铃")
    点击麦克风()
def 播放考试铃():
    点击麦克风()
    PlayBell("考试铃.mp3")
    print("播放考试铃")
    点击麦克风()
def 播放眼保健操():
    点击麦克风()
    PlayBell("眼保健操.mp3")
    print("播放眼保健操")
    点击麦克风()
def 音乐时长(path):
    if ".mp3" in path:
        return MP3(path).info.length
    elif ".flac" in path:
        return FLAC(path).info.length
    elif ".ogg" in path:
        return OggVorbis(path).info.length  
def 筛选异常音乐():
    try:
        fileList = os.listdir(r"未放")
        #网易云音乐(ncm)，QQ音乐(qmc、mflac、mgg)，酷狗音乐(kgm)，虾米音乐(xm)，酷我音乐(kwm)
        for i in fileList:
            if ".mflac" in i or ".mgg" in i or ".qmc" in i or ".kgm" in i or ".xm" in i or ".kwm" in i or ".ncm" in i:
                oldMusicPath = "未放\\" + i
                newMusicPath = "异常\\" + i
                print("处理格式异常音乐",i)
                pt.say("处理格式异常音乐")
                pt.say(i)
                pt.runAndWait()
                shutil.move(oldMusicPath,newMusicPath)
            else:
                try:
                    MusicPath = "未放\\" + i
                    if  音乐时长(MusicPath) == None:
                        oldMusicPath = "未放\\" + i
                        newMusicPath = "异常\\" + i
                        print("处理属性异常音乐",i)
                        pt.say("处理属性异常音乐")
                        pt.say(i)
                        pt.runAndWait()
                        shutil.move(oldMusicPath,newMusicPath)

                except:
                    #oldMusicPath = "D:\\FTP\\未放\\" + i
                    #newMusicPath = "D:\\FTP\\异常\\" + i
                    #shutil.move(oldMusicPath,newMusicPath)
                    print("音乐属性检测失败")
    except:
        print("未能成功筛选音乐")
        pt.say("未能成功筛选音乐")
        pt.runAndWait()
def 播放音乐():
    global a
    筛选异常音乐()
    time.sleep(0.1)
    try:
        musicPath = "压根没抽出来"
        fileList = os.listdir(r"未放")
        listLenth = len(fileList)
        n = random.randint(0,listLenth)
        musicPath = fileList[n]
        print(musicPath)
        oldMusicPath = "未放\\" + musicPath
        newMusicPath = "已放\\" + musicPath
        wrongMusicPath = "异常\\" + musicPath
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
def WhetherPlayMusic(d,t,Mode):       
    if 1 in Mode:
        if d == 1:
            if t in StudyStart1:
                播放上课铃()
                time.sleep(60)
            if t in StudyEnd1:
                播放下课铃()
                time.sleep(60)
            if t in MusicTime15:
                点击麦克风()
                x=1
                T=0
                while T < 900:
                    print("准备播放第",x,"首歌")
                    x+=1
                    播放音乐()
                    T += a
                    print("已经播放 =",T,"秒")
                点击麦克风()
            if t in MusicTime1:
                点击麦克风()
                播放音乐()
                点击麦克风()
        if d != 1:
            if t in StudyStart23456:
                播放上课铃()
                time.sleep(60)
            if t in StudyEnd23456:
                播放下课铃()
                time.sleep(60)
            if t in MusicTime15:
                点击麦克风()
                x=1
                T=0
                while T < 900:
                    print("准备播放第",x,"首歌")
                    x+=1
                    播放音乐()
                    T += a
                    print("已经播放 =",T,"秒")
                点击麦克风()
            if t in MusicTime1:
                点击麦克风()
                播放音乐()
                点击麦克风()
    else:
        if t in TestTime:
            播放考试铃()
            time.sleep(30)
try:
    f=open('TimeTable.txt',encoding = "utf-8")
    timeTable = f.readlines()
    #print(timeTable)
    mode = timeTable[0].replace("\\n","").split()
    Mode = [int(x) for x in mode]
    mousePlace = timeTable[1].replace("\\n","").split()
    MousePlace = [int(x) for x in mousePlace]
    studyStart1 = timeTable[2].replace("\\n","").split()
    StudyStart1 = [int(x) for x in studyStart1]
    studyStart23456 = timeTable[3].replace("\\n","").split()
    StudyStart23456 = [int(x) for x in studyStart23456]
    studyEnd1 = timeTable[4].replace("\\n","").split()
    StudyEnd1 = [int(x) for x in studyEnd1]
    studyEnd23456 = timeTable[5].replace("\\n","").split()
    StudyEnd23456 = [int(x) for x in studyEnd23456]
    musicTime15 = timeTable[6].replace("\\n","").split()
    MusicTime15 = [int(x) for x in musicTime15]
    musicTime1 = timeTable[7].replace("\\n","").split()
    MusicTime1 = [int(x) for x in musicTime1]
    testTime = timeTable[8].replace("\\n","").split()
    TestTime = [int(x) for x in testTime]
    print("模式:",Mode)
    print("麦克风按钮坐标:",MousePlace)
    print("周一上课铃播放时间:",StudyStart1)
    print("上课铃播放时间:",StudyStart23456)
    print("周一下课铃播放时间:",StudyEnd1)
    print("下课铃播放时间=",StudyEnd23456)
    print("15分钟音乐播放开始时间=",MusicTime15)
    print("单首音乐播放时间=",MusicTime1)
    print("考试铃声播放时间=",testTime)
    print("星期:",int(time.strftime("%w")))
    f.close()
except:
    print("TimeTable读取异常,请检查你的输入")
    time.sleep(60)

while 1:
    t = int(time.strftime("%H%M"))
    d = int(time.strftime("%w"))
    print(t)   
    WhetherPlayMusic(d,t,Mode)
    time.sleep(10)
```
