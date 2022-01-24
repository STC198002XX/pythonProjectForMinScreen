# 這個py是用來整合所有功能在一個執行檔
import alarm
import StartStatusCheck
import quene_to_play
import integrated


def finall():
    print("<A>:測試撥skype功能是否正常")
    print("<B>:測試目前程式能偵測到幾個角色在省電模式中")
    print("<C>:執行排隊偵測，將於排完隊後撥打skype提醒，此程式每分鐘偵測一次")
    print("<D>:執行角色是否正在賺錢，發現有角色於一分鐘內金幣沒有增加，會撥打skype提醒，此程式每半小時執行一次，直到使用者關閉視窗")
    print("<Q>:結束程式")
    command = input("請輸入對應的大寫字母後按ENTER執行:")
    if command == "A":
        alarm.call()
    elif command == "B":
        StartStatusCheck.scan()
    elif command == "C":
        quene_to_play.quene()
    elif command == "D":
        integrated.integrate()
    elif command == "Q":
        pass
    else:
        finall()


finall()
