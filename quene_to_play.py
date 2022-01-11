import pyautogui
import winsound
import time

number = len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG')))
print(number)

while len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG'))) == number:
    time.sleep(60)

pyautogui.click(pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'))

