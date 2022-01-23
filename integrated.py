import monitor
import alarm
import time
import time_recorded

while True:
    a = monitor.check()   # 沒在賺錢的角色數量。
    if a == 0:

        print(f"在遊戲中的角色都在賺錢     "+time_recorded.time_message()+"\n")

    else:
        print(f"在遊戲中的角色有{a}個沒有在賺錢     " + time_recorded.time_message())
        print("呼叫撥打電話的程式中     "+time_recorded.time_message())
        alarm.call()     # 打電話
    time.sleep(1800)
