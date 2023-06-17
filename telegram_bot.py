import schedule
import time
import telegram
import datetime

# token = "5694552958:AAHAbb4b9nVv299nPutd8OVn-KPyOWfotSw"
# chat_id = "5592503813"
# public_chat_name = "@AltOsbb"

token = "5694552958:AAHAbb4b9nVv299nPutd8OVn-KPyOWfotSw"
bot = telegram.Bot(token=token)
chat_id = "5592503813"
updates = bot.get_updates()

def job():
    now_local = datetime.datetime.now()
    now_local_time = now_local.strftime("%Y-%m-%d %H:%M:%S")
    
    # 특정 시간 회피
    if now_local.strftime("%H") >= "23" or now_local.strftime("%H") <= "6":
        pass
    bot.sendMessage(chat_id=chat_id, text=('지금은 ' + str(now_local_time) + ' 야'))

schedule.every(0).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)