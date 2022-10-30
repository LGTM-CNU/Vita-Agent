import time
import threading
from pytz import timezone
from datetime import date, datetime
from ttsKorean import saying
from speechToText import speechToText

alarmList = [
		{'type': 'C', 'date': datetime(2022,10,30,17,32)},
		{'type': 'B2', 'date': datetime(2022,10,30,16,37)},
		{'type': 'B1', 'date': datetime(2022, 10, 27, 21, 37)}
	]

def conversation():
	now = datetime.now(timezone('Asia/Seoul'))
	print('last 40 sec...')
	for i in alarmList:
		if now.year == i['date'].year and now.month == i['date'].month and now.day == i['date'].day and  now.hour == i['date'].hour and now.minute == i['date'].minute:
			saying('비타민 드셨나요?')
			client_answer = speechToText()
			if client_answer == 'yes':
				saying('잘하셨어요')
			elif client_answer == 'no':
				saying('비타민을 복약해야합니다.')
			elif client_answer == 'hello':
				saying('안녕하세요 비타입니다.')
			elif client_answer == 'bye':
				saying('종료합니다.')
				exit()

def alarm():
	conversation()
	threading.Timer(40, alarm).start()


print('Vita Start')
alarm()
