import pyautogui
import pydirectinput
import random
# import click_through_arduino
import time
position = pyautogui.locateAllOnScreen(r'for_autoclick\maximize.png')


def unlock(x,y):
    pyautogui.moveTo(x-135, y+172, duration=random.randint(3, 5))
    # click_through_arduino.press_down()
    pyautogui.dragTo(x + 127, y + 83,duration=0.5)
    # click_through_arduino.press_up()
def receive_signin_reward(x,y):
    # click_through_arduino.click()
    print(1)
    pyautogui.moveTo(x + 106, y + 29, duration=random.randint(3, 5))
    time.sleep(5)
    pyautogui.click(x + 300, y + 29)
    # click_through_arduino.click()
    # pydirectinput.moveTo(x+500,y)
    print(2)
    pyautogui.moveTo(x + 62, y + 89, duration=random.randint(3, 5))
    # click_through_arduino.click()
    print(3)
    time.sleep(5)
    pyautogui.moveTo(x + 75, y + 135, duration=random.randint(3, 5))
    # click_through_arduino.click()


for i in position:
    x = round(i[0]+i[2]/2)
    y = round(i[1]+i[3]/2)
    receive_signin_reward(x, y)

