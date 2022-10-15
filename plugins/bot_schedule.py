import schedule
import datetime
import time
import threading
import genshin_sign

schedule.every().day.at("1:20").do(genshin_sign.sign_daily)



def schedule_start():
    print("定时任务开始执行 at " + str(datetime.datetime.now()))
    while 1:
        schedule.run_pending()
        time.sleep(1)

t1 = threading.Thread(name="t1", target=schedule_start, daemon=True)
t1.start()