import monitor
import alarm

a = monitor.check()   # 沒在賺錢的角色數量。
print(a)
if a > 0:
    alarm.call()     # 打電話
