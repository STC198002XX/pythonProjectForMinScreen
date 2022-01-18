import pyautogui


def call():
    print("撥打電話程式執行中")
    pyautogui.click(pyautogui.locateCenterOnScreen(r'for_quene/call.PNG'))


if __name__ == '__main__':
    call()