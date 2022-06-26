from skpy import Skype    # 用skpy的package(非官方的)
import time_recorded

with open(r"c:\data_for_python.txt", "rt", encoding="utf-8") as data:
    txt = data.read().split()
    print(txt)


def send_message(a, n):
    sk = Skype(txt[2], txt[3])
    contacts = sk.contacts # sk的聯絡人
    for i in contacts:  # 把聯絡人都列出來，可以查到他們的ID
        print(i)
    aaa = sk.contacts[txt[4]]  # 聯絡人物件
    aaa.chat.sendMsg(f"第{n}次連續警報:有{a}個人沒在賺錢     "+time_recorded.time_message())    # 送簡訊給這個聯絡人


def send_message_string(s):
    sk = Skype(txt[2], txt[3])
    contacts = sk.contacts # sk的聯絡人
    for i in contacts:  # 把聯絡人都列出來，可以查到他們的ID
        print(i)
    aaa = sk.contacts[txt[4]]  # 聯絡人物件
    aaa.chat.sendMsg(f"{s}     "+time_recorded.time_message())    # 送簡訊給這個聯絡人


if __name__=="__main__":
    send_message_string("我程式又變強了")

