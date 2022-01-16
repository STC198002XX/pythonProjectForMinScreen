import monitor
import alarm
import time

while True:
    a = monitor.check()   # 沒在賺錢的角色數量。
    print(a)
    if a > 0:
        alarm.call()     # 打電話
    time.sleep(1800)
