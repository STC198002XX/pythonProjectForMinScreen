import pyautogui
import winsound
import time
import pyscreenshot
'''
input("在要抓的畫面左上角後按enter")
x1, y1 =pyautogui.position()
print(x1, y1)

input("在要抓的畫面右下角後按enter")
x2, y2 = pyautogui.position()
print(x2, y2)
'''
'''
for i in range(10):
    winsound.Beep(1000+100*i,1000)
'''

pyautogui.click(pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'))