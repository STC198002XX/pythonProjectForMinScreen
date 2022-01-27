import monitor
import alarm
import time
import time_recorded
import send_skype_message


def integrate():
    n = 0  # 連續警報的次數
    while True:
        a = monitor.check()   # 沒在賺錢的角色數量。
        if a == 0:
            n = 0
            print(f"在遊戲中的角色都在賺錢     "+time_recorded.time_message()+"\n")

        else:
            n += 1
            print(f"在遊戲中的角色有{a}個沒有在賺錢     " + time_recorded.time_message())
            # print("呼叫撥打電話的程式中     "+time_recorded.time_message())
            # alarm.call()     # 打電話
            print("呼叫送skype簡訊的程式中     "+time_recorded.time_message())
            send_skype_message.send_message(a, n)
        time.sleep(1800)


if __name__ == '__main__':
    integrate()