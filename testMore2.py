import pyautogui

a = pyautogui.locateAllOnScreen(r"for_arduino\square.png")
for i in a:
    print(i)

while True:
    a = input("按enter讀位置")
    if a == "Q":
        break
    print(pyautogui.position())