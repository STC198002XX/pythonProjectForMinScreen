import pyautogui
import time

# number = 0
# for box in pyautogui.locateAllOnScreen(r"for_diamond_calculating\full_screen.png"):
#     pyautogui.click(box[0]+box[2]//2, box[1]+box[3]//2)
#     time.sleep(2)
#     pyautogui.click(pyautogui.locateCenterOnScreen(r"for_diamond_calculating\min_screen.png"))
#     time.sleep(2)
#     number += 1
#     print(box)
# print(number)

time.sleep(3)
pyautogui.mouseDown()
time.sleep(1)
pyautogui.mouseUp()
