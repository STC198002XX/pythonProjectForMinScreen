import pyfirmata
import time
board = pyfirmata.Arduino('COM6')
print("Communication Successfully started")


def click():
    board.digital[7].write(1)
    time.sleep(5)
    board.digital[7].write(0)
    time.sleep(1)


def drag_to_right():
    board.digital[7].write(1)
    time.sleep(0.5)
    board.digital[6].write(1)
    time.sleep(0.5)
    board.digital[6].write(0)
    board.digital[7].write(0)
    time.sleep(1)



def move_to_right():
    board.digital[6].write(1)
    time.sleep(0.5)
    board.digital[6].write(0)
    time.sleep(1)


def press_down():  #按下滑鼠左鍵
    board.digital[7].write(1)
    time.sleep(0.5)


def press_up():  #放開滑鼠左鍵
    board.digital[7].write(0)
    time.sleep(1)



if __name__ == "__main__":
    time.sleep(1)
    drag_to_right()
