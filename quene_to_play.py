import pyautogui
import time
import alarm
import time_recorded

def quene():
    print("程式將於5秒後開始偵測，請勿讓本視窗擋住要偵測的畫面     "+ time_recorded.time_message())
    time.sleep(5)
    number = len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG')))
    if number == 0:
        print("沒有偵測到排隊中的角色，程式將於10秒鐘後自動關閉     "+time_recorded.time_message())
        time.sleep(10)
    else:
        print(f'偵測到{number}個人物排隊中     '+ time_recorded.time_message())

        time_start = time.time()

        while len(list(pyautogui.locateAllOnScreen(r'for_quene/quene.PNG'))) == number:
            print(f'程式偵測已經過{round(time.time()-time_start)}秒鐘     '+ time_recorded.time_message())
            time.sleep(60)
        print("呼叫撥電話程式中     " + time_recorded.time_message())
        alarm.call()
        print("程式將於5秒後自動關閉     " + time_recorded.time_message())
        time.sleep(5)
        # pyautogui.click(pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'))


if __name__ == '__main__':
    quene()

