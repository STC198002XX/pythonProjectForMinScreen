import click_through_arduino
import pyautogui
import time
import random
print(random.randint(-2, 2))
pyautogui.FAILSAFE = False


def restock_the_good_function(x, y):
    a = [x, y]

    # define the relative position (from experience)
    relative_unlock_loctaion = [-81, 131]
    relative_hamberger_button = [106, 29]
    relatvie_auction_button = [39, 89]
    relatvie_sell_button = [-186, 49]
    relatvie_restock_the_failed_good =[-20, 227]
    relative_restock = [-51, 203]
    relative_cancel_restock = [-112, 203]
    relative_confirm = [-80, 204]

    relatvie_exit_auction = [95, 31]
    relative_quick_set = [-266, 179]
    relative_auto_huntering = [-83, 131]

    # define buttons
    unlock_loctaion = [a[0]+relative_unlock_loctaion[0]+random.randint(-50, 50), a[1]+relative_unlock_loctaion[1]+random.randint(-50, 50)]
    hamberger_button = [a[0]+relative_hamberger_button[0]+random.randint(-2, 2), a[1]+relative_hamberger_button[1]+random.randint(-2, 2)]
    auction_button = [a[0]+relatvie_auction_button[0]+random.randint(-2, 2), a[1]+relatvie_auction_button[1]+random.randint(-2, 2)]
    sell_button = [a[0]+relatvie_sell_button[0]+random.randint(-10, 10), a[1]+relatvie_sell_button[1]+random.randint(-2, 2)]
    restock_the_failed_good = [a[0]+relatvie_restock_the_failed_good[0]+random.randint(-10, 10),a[1]+relatvie_restock_the_failed_good[1]+random.randint(-2, 2)]
    restock = [a[0]+relative_restock[0]+random.randint(-10, 10), a[1]+relative_restock[1]+random.randint(-2, 2)]
    cancel_restock = [a[0]+relative_cancel_restock[0]+random.randint(-10, 10), a[1]+relative_cancel_restock[1]+random.randint(-2, 2)]
    confirm = [a[0]+relative_confirm[0]+random.randint(-10, 10), a[1]+relative_confirm[1]+random.randint(-2, 2)]

    exit_auction = [a[0]+relatvie_exit_auction[0]+random.randint(-2, 2), a[1]+relatvie_exit_auction[1]+random.randint(-2, 2)]
    quick_set = [a[0]+relative_quick_set[0]+random.randint(-1, 3), a[1]+relative_quick_set[1]+random.randint(-2, 2)]
    auto_huntering = [a[0]+relative_auto_huntering[0]+random.randint(-20, 20), a[1]+relative_auto_huntering[1]+random.randint(-20, 20)]

    def exit_the_control_of_simulator(): # 要離開模擬器的控制，pyautogui才能控制滑鼠座標
        print("執行離開模擬器的控制程序中")
        present_location = pyautogui.position()
        while present_location[0] < 1633: # 沒有到右邊沒模擬器的地方就不要按
            click_through_arduino.move_to_right()
            time.sleep(1)
            present_location = pyautogui.position()
        click_through_arduino.click()

    print("正移動到要解鎖的位置")
    pyautogui.moveTo(*unlock_loctaion, duration=1)
    print("正要解鎖自動狩獵模式")
    click_through_arduino.drag_to_right()
    exit_the_control_of_simulator()

    # 按漢堡的按鈕
    print("執行按漢堡的程序")
    pyautogui.moveTo(*hamberger_button, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    # 按交易所的按鈕
    print("執行按交易所的程序")
    pyautogui.moveTo(*auction_button, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    # 按販售的按鈕
    print("執行按販售的程序")
    pyautogui.moveTo(*sell_button, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    if pyautogui.locateCenterOnScreen(r"for_arduino\fail_to_sell.png"): # 這裡還沒寫完
        print("有東西販售失敗")

        # 按販售失敗重新登錄的按鈕
        print("執行按販售失敗重新登錄的程序")
        pyautogui.moveTo(*restock_the_failed_good, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

        print("執行按重新登錄的程序")
        pyautogui.moveTo(*restock, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()
        time.sleep(3)
        if pyautogui.locateCenterOnScreen(r"for_arduino\cancel_restock_button.png"):
           print(f"重新登錄的圖示還在，要傳簡訊了,position為({x},{y})的包包滿了")
           print("執行按取消重新登錄的程序")
           pyautogui.moveTo(*cancel_restock, duration=1)
           click_through_arduino.click()
           exit_the_control_of_simulator()
        else:
            print(f"重新登錄的圖示消失，等待確認的按鈕出現")
            while not pyautogui.locateCenterOnScreen(r"for_arduino\confirm.png"):
                time.sleep(5)
            print("執行按確認的程序")
            pyautogui.moveTo(*confirm, duration=1)
            click_through_arduino.click()
            exit_the_control_of_simulator()


    # 按離開交易所的按鈕
    print("執行離開交易所的程序")
    pyautogui.moveTo(*exit_auction, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    # 按快速設定的按鈕
    print("執行按快速設定的程序")
    pyautogui.moveTo(*quick_set, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    # 按自動狩獵的按鈕
    print("執行按自動狩獵的程序")
    pyautogui.moveTo(*auto_huntering, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

if __name__ == '__main__':
    input("把滑鼠游標放在要執的框框後按enter")
    position = pyautogui.position()
    restock_the_good_function(position[0], position[1])



