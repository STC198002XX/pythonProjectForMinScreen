import pyautogui
import time
import pydirectinput
import time_recorded


def call():

    if pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'):
        print("撥打電話程式執行中     " + time_recorded.time_message())
        x, y = pyautogui.locateCenterOnScreen(r'for_quene/call.PNG')
        pydirectinput.moveTo(x, y)  # pydirectinput沒有duration的功能
        time.sleep(1)
        pydirectinput.click()
        print("已撥打電話     " + time_recorded.time_message() + "\n")
    else:
        print("偵測不到撥打skype的圖示，請調整畫面後再使用本功能     " + time_recorded.time_message())



if __name__ == '__main__':
    call()

