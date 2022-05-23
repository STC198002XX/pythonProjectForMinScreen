import pyautogui
import restock_auction
all_account_position = pyautogui.locateAllOnScreen(r'for_arduino\square.png')
for position in all_account_position:
    x = position[0]+position[2]//2
    y = position[1]+position[3]//2
    # print(f'{position}  x:{x}  y:{y}')
# for x, y in all_account_position:
    restock_auction.restock_the_good_function(x, y)