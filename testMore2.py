import pyautogui
# while 1:
#     enter = input("寫任何註解後，把滑鼠移到要紀錄的位置後按enter(q for leave):")
#     if enter == "q":
#         break
#     print(pyautogui.position())
position = pyautogui.locateAllOnScreen(r'for_autoclick\maximize.png')
for i in position:
    print(i)
print(pyautogui.locateCenterOnScreen(r'for_autoclick\maximize.png'))