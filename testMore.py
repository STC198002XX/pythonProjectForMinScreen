from skpy import Skype    # 用skpy的package(非官方的)
sk = Skype("SignForAlarm1@outlook.com", '密碼')
contacts = sk.contacts # sk的聯絡人
for i in contacts:  # 把聯絡人都列出來，可以查到他們的ID
    print(i)
aaa = sk.contacts['live:lspropane']  # 聯絡人物件
aaa.chat.sendMsg("test skpy")    # 送簡訊給這個聯絡人

