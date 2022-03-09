import time
import os
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import pyperclip
m=PyMouse()
k=PyKeyboard()
os.startfile("铃声播放.py")
os.startfile("C:\\Program Files (x86)\\Tencent\\WeMeet\\wemeetapp.exe")
time.sleep(5)
m.click(626,218)
time.sleep(1)
pyperclip.copy("217-361-788")
k.press_keys([k.control_key,"v"])
time.sleep(1)
k.tap_key(k.enter_key)
time.sleep(3)
m.click(1201, 105)
