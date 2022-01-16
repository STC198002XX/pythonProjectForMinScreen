import pyautogui
import time
import alarm

number = len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG')))
print(number)

time_start = time.time()

while len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG'))) == number:
    print(time.time()-time_start)
    time.sleep(60)

alarm.call()

# pyautogui.click(pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'))

