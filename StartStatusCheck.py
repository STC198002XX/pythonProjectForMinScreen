import pyautogui
import pyscreenshot as ImageGrab
import cv2
# 對螢幕截圖
img = ImageGrab.grab()
# 截圖存檔
img.save(r'for_detecting_no_make_money\fullscreen.png')
# 把存的檔取出來，要做存檔再存檔的原因是上面存檔的模組是pyscreenshot，下面讀檔的模組是opencv
img1 = cv2.imread(r'for_detecting_no_make_money\fullscreen.png')


position = pyautogui.locateAllOnScreen("money_mark.PNG")
# 因為上面locateAllOnScreen的函數回傳的是generator，無法直接取其數量，所以設deviceNumber取數量
deviceNumber = 0

for i in position:
    deviceNumber += 1
    # 因為上面locateAllOnScreen回傳的物件是Box(左上x,左上y,寬,高)，下面畫寬時+50把錢的數字包進去)
    cv2.rectangle(img1, (i[0], i[1]), (i[0]+i[2]+50, i[1]+i[3]), (0, 255, 0), 2)

img1 = cv2.resize(img1, (0, 0), fx=0.75, fy=0.75)
cv2.putText(img1, f'{deviceNumber} characters detected', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow(f'{deviceNumber} characters detected', img1)
cv2.waitKey(0)

