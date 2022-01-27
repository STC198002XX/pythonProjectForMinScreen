from skpy import Skype    # 用skpy的package(非官方的)
import time_recorded

def send_message(a, n):
    sk = Skype("SignForAlarm1@outlook.com", 'lineageW.alarm1')
    contacts = sk.contacts # sk的聯絡人
    for i in contacts:  # 把聯絡人都列出來，可以查到他們的ID
        print(i)
    aaa = sk.contacts['live:lspropane']  # 聯絡人物件
    aaa.chat.sendMsg(f"第{n}次連續警報:有{a}個人沒在賺錢     "+time_recorded.time_message())    # 送簡訊給這個聯絡人

if __name__=="__main__":
    send_message(100)

