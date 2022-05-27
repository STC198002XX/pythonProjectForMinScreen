import pyautogui
import buy_the_enhancing_scroll
all_account_position = pyautogui.locateAllOnScreen(r'for_arduino\square.png')
for position in all_account_position:
    x = position[0]+position[2]//2
    y = position[1]+position[3]//2
    # print(f'{position}  x:{x}  y:{y}')
# for x, y in all_account_position:
    buy_the_enhancing_scroll.buy_the_scrolls(x, y)