# 說明:這個模組在被執行時會標出沒有賺錢的角色，而被import且執行check()時，會回傳一個數字，
# 為沒有在賺錢的角色數量。

import pyautogui
import pyscreenshot as ImageGrab
import cv2
import time
import time_recorded

def check():
    # 對螢幕截圖
    img = ImageGrab.grab()
    # 截圖存檔
    img.save(r'for_detecting_no_make_money\fullscreen.png')
    # 把存的檔取出來，要做存檔再存檔的原因是上面存檔的模組是pyscreenshot，下面讀檔的模組是opencv
    img1 = cv2.imread(r'for_detecting_no_make_money\fullscreen.png')
    # 要畫紅線的
    # img2 = img1.copy()

    # 這裡是用已存下


    position = pyautogui.locateAllOnScreen("money_mark.PNG")
    # 因為上面locateAllOnScreen的函數回傳的是generator，無法直接取其數量，所以設deviceNumber取數量
    deviceNumber = 0
    locationRecord = []
    for i in position:
        deviceNumber += 1
        locationRecord.append([i[0], i[1], i[0] + i[2] + 50, i[1] + i[3]])
        picture = ImageGrab.grab(bbox=(i[0], i[1], i[0]+i[2]+50, i[1]+i[3]))
        # print([i[0], i[1], i[0]+i[2]+50, i[1]+i[3]])

        picture.save(rf'for_detecting_no_make_money\picture{deviceNumber}.png')
        cv2.rectangle(img1, (i[0], i[1]), (i[0]+i[2]+50, i[1]+i[3]), (0, 255, 0), 2)
    # 下面這行只是確認有資料
    # print(locationRecord)
    #print(f'偵測到{deviceNumber}個角色在遊戲中     monitor.py'+time_recorded.time_message())
    # img1 = cv2.resize(img2, (0, 0), fx=0.75, fy=0.75)
    # cv2.imshow(f'{deviceNumber} characters detected', img1)
    # cv2.waitKey(0)
    DetectedNumber = 0
    time.sleep(60)

    # 對螢幕截圖
    img2 = ImageGrab.grab()
    # 截圖存檔
    img2.save(r'for_detecting_no_make_money\fullscreen2.png')
    # 把存的檔取出來，要做存檔再存檔的原因是上面存檔的模組是pyscreenshot，下面讀檔的模組是opencv
    img2 = cv2.imread(r'for_detecting_no_make_money\fullscreen2.png')

    for j in range(deviceNumber):
        if not (pyautogui.locateOnScreen(rf'for_detecting_no_make_money\picture{j+1}.png')):
            #print(pyautogui.locateOnScreen(rf'for_detecting_no_make_money\picture{j+1}.png'))
            DetectedNumber += 1



    return DetectedNumber  #check這個函式會回傳沒有在賺錢的人物


if __name__ == '__main__':
    check()

