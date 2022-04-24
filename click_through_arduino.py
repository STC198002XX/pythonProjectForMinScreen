import pyfirmata
import time
board = pyfirmata.Arduino('COM5')
print("Communication Successfully started")


def click():
    board.digital[7].write(1)
    time.sleep(0.5)
    board.digital[7].write(0)
    time.sleep(1)


def press_down():  #按下滑鼠左鍵
    board.digital[7].write(1)
    time.sleep(0.5)


def press_up():  #放開滑鼠左鍵
    board.digital[7].write(0)
    time.sleep(1)



if __name__ == "__main__":
    click()