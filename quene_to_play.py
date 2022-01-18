import pyautogui
import time
import alarm

number = len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG')))
print(f'偵測到{number}個人物排隊中')

time_start = time.time()

while len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG'))) == number:
    print(f'程式執行已經過{round(time.time()-time_start)}秒鐘')
    time.sleep(60)
print("呼叫撜電話程式中")
alarm.call()
print("程式將於5秒後自動關閉")
time.sleep(5)
# pyautogui.click(pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'))

