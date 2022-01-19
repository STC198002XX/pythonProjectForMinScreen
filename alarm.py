import pyautogui
import time

def call():
    print("撥打電話程式執行中")
    pyautogui.moveTo(pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'), duration=2)
    time.sleep(1)
    pyautogui.click()


if __name__ == '__main__':
    call()