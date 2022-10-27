import time
import threading
from pytz import timezone
from datetime import date, datetime
from tts import saying
from speechToText import speechToText

alarmList = [
		{'type': 'C', 'date': datetime(2022,10,27,21,49)},
		{'type': 'B2', 'date': datetime(2022, 10,27,21,40)},
		{'type': 'B1', 'date': datetime(2022, 10, 27, 21, 37)}
	]

def conversation():
	now = datetime.now(timezone('Asia/Seoul'))
	print('last 40 sec...')
	for i in alarmList:
		if now.year == i['date'].year and now.month == i['date'].month and now.day == i['date'].day and  now.hour == i['date'].hour and now.minute == i['date'].minute:
			saying('alarm')
			client_answer = speechToText()
			if client_answer == 'yes':
				saying('good')
			elif client_answer == 'no':
				saying('not good')
			elif client_answer == 'hello':
				saying('hello')
			elif client_answer == 'bye':
				saying('ok bye')
				exit()

def alarm():
	conversation()
	threading.Timer(40, alarm).start()


print('Vita Start')
alarm()
