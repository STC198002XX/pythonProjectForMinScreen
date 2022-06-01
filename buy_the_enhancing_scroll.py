import click_through_arduino
import pyautogui
import time
import random
print(random.randint(-2, 2))
pyautogui.FAILSAFE = False


def buy_the_scrolls(x, y):
    a = [x, y]

    # define the relative position (from experience)
    relative_unlock_loctaion = [-81, 131]
    relative_shop_location = [15, 31]
    relative_xx_of_googlePlay = [103, 37]
    relative_dontShowToday = [-236, 206]
    relative_confirm_to_cancel = [-79, 158]
    relative_exchange_of_goods = [-187, 50]
    relative_consumables = [-257, 92]
    relative_weapon_scroll = [-162, 111]
    relative_add_ten = [-129, 158]
    relative_confirm_to_buy = [-52, 193]
    relative_armor_scroll = [-162, 198]
    relative_exit_the_shop = [101, 31]




    relative_quick_set = [-266, 179]
    relative_auto_huntering = [-83, 131]

    # define buttons
    unlock_loctaion = [a[0]+relative_unlock_loctaion[0]+random.randint(-50, 50), a[1]+relative_unlock_loctaion[1]+random.randint(-50, 50)]
    shop_location = [a[0]+relative_shop_location[0]+random.randint(-2, 2), a[1]+relative_shop_location[1]+random.randint(-2, 2)]
    xx_of_googlePlay = [a[0]+relative_xx_of_googlePlay[0]+random.randint(-2, 2), a[1]+relative_xx_of_googlePlay[1]+random.randint(-2, 2)]
    dontShowToday = [a[0]+relative_dontShowToday[0]+random.randint(-20, 20), a[1]+ relative_dontShowToday[1]+random.randint(-2, 2)]
    confirm_to_cancel = [a[0]+relative_confirm_to_cancel[0]+random.randint(-20, 20), a[1]+relative_confirm_to_cancel[1]+random.randint(-2, 2)]
    exchange_of_goods = [a[0]+relative_exchange_of_goods[0]+random.randint(-20, 20), a[1]+relative_exchange_of_goods[1]+random.randint(-2, 2)]
    consumables = [a[0]+relative_consumables[0]+random.randint(-10, 10), a[1]+relative_consumables[1]+random.randint(-2, 2)]
    weapon_scroll = [a[0]+relative_weapon_scroll[0]+random.randint(-20, 20), a[1]+relative_weapon_scroll[1]+random.randint(-20, 20)]
    add_ten = [a[0]+relative_add_ten[0]+random.randint(-2, 2), a[1]+relative_add_ten[1]+random.randint(-2, 2)]
    confirm_to_buy = [a[0]+relative_confirm_to_buy[0]+random.randint(-20, 20), a[1]+relative_confirm_to_buy[1]+random.randint(-2, 2)]
    armor_scroll = [a[0] + relative_armor_scroll[0] + random.randint(-20, 20), a[1] + relative_armor_scroll[1] + random.randint(-20, 20)]
    exit_the_shop = [a[0] + relative_exit_the_shop[0] + random.randint(-2, 2), a[1] + relative_exit_the_shop[1] + random.randint(-2, 2)]




    quick_set = [a[0]+relative_quick_set[0]+random.randint(-1, 3), a[1]+relative_quick_set[1]+random.randint(-2, 2)]
    auto_huntering = [a[0]+relative_auto_huntering[0]+random.randint(-30, 30), a[1]+relative_auto_huntering[1]+random.randint(-30, 30)]

    def exit_the_control_of_simulator(): # 要離開模擬器的控制，pyautogui才能控制滑鼠座標
        print("執行離開模擬器的控制程序中")
        present_location = pyautogui.position()
        time.sleep(1)
        new_present_location = pyautogui.position()
        while (present_location[0] < 1633) or (present_location[0] != new_present_location[0]) or (present_location[1] != new_present_location[1])  : # 沒有到右邊沒模擬器的地方就不要按
            click_through_arduino.move_to_right()
            time.sleep(1)
            present_location = pyautogui.position()
            time.sleep(1.5)
            new_present_location = pyautogui.position()
        click_through_arduino.click()

    print("正移動到要解鎖的位置")
    pyautogui.moveTo(*unlock_loctaion, duration=1)
    print("正要解鎖自動狩獵模式")
    click_through_arduino.drag_to_right()
    exit_the_control_of_simulator()

    while pyautogui.locateCenterOnScreen(r"for_arduino\home_scroll.png") == None:
        print("沒有看到home_scroll，再等5秒鐘")
        time.sleep(5)
        print("正移動到要解鎖的位置")
        pyautogui.moveTo(*unlock_loctaion, duration=1)
        print("正要解鎖自動狩獵模式")
        click_through_arduino.drag_to_right()
        exit_the_control_of_simulator()

    # 按商城的按鈕
    print("執行按商城的程序")
    pyautogui.moveTo(*shop_location, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    if pyautogui.locateCenterOnScreen(r"for_arduino\googlePlay.png"): # 這裡還沒寫完
        print("googlePlay的圖示跳出了")

        print("執行按右上XX的程序")
        pyautogui.moveTo(*xx_of_googlePlay, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

    if pyautogui.locateCenterOnScreen(r"for_arduino\dontShowTodayShop.png"): # 這裡還沒寫完
        print("今天不再顯示的圖示跳出了")

        print("執行按今天不再顯示的圖示")
        pyautogui.moveTo(*dontShowToday, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

    # 按確認_已取消變更付費帳號的按鈕
    print("執行按確認_已取消變更付費帳號的按鈕")
    pyautogui.moveTo(*confirm_to_cancel, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    # 按交換所的按鈕
    print("執行按交換所的按鈕")
    pyautogui.moveTo(*exchange_of_goods, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    # 按消耗品的按鈕
    print("執行按消耗品的按鈕")
    pyautogui.moveTo(*consumables, duration=1)
    click_through_arduino.click()
    exit_the_control_of_simulator()

    if pyautogui.locateCenterOnScreen(r"for_arduino\weapon_scroll_available.png"): # 這裡還沒寫完
        print("今天的武卷還沒買完")
        # 按買武卷的按鈕
        print("執行按買武卷的按鈕")
        pyautogui.moveTo(*weapon_scroll, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

        # 按加十的按鈕
        print("執行按加十的按鈕")
        pyautogui.moveTo(*add_ten, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

        # 按買的確認按鈕
        print("執行按買的確認按鈕")
        pyautogui.moveTo(*confirm_to_buy, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

    if pyautogui.locateCenterOnScreen(r"for_arduino\armor_scroll_available.png"): # 這裡還沒寫完
        print("今天的防卷還沒買完")

        # 按買防卷的按鈕
        print("執行按買防卷的按鈕")
        pyautogui.moveTo(*armor_scroll, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

        # 按加十的按鈕
        print("執行按加十的按鈕")
        pyautogui.moveTo(*add_ten, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()

        # 按買的確認按鈕
        print("執行按買的確認按鈕")
        pyautogui.moveTo(*confirm_to_buy, duration=1)
        click_through_arduino.click()
        exit_the_control_of_simulator()


    # 按離開商店的按鈕
    print("執行按離開商店的按鈕")
    pyautogui.moveTo(*exit_the_shop, duration=1)
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
    buy_the_scrolls(position[0], position[1])



