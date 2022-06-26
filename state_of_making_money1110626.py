import monitor2
import send_skype_message
import time
while True:
    making_money_number = monitor2.check()
    with open(r"c:\data_for_python.txt", "rt", encoding="utf-8") as data:
        txt = data.read().split()

    number_created = int(txt[5])
    print(f'賺錢人物/所有人物:{making_money_number}/{number_created}')
    send_skype_message.send_message_string(f'賺錢人物/所有人物:{making_money_number}/{number_created}')
    time.sleep(3600)