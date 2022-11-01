import time
from threading import Timer, Thread
from pytz import timezone
from datetime import date, datetime
from util.tts import say
from util.speechToText.speechToText import listen

volume = 0.1

alarmList = [
		{'type': 'C', 'date': datetime(2022,11,1,12,8)},
		{'type': 'B', 'date': datetime(2022,10,30,16,37)},
		{'type': 'B', 'date': datetime(2022, 10, 27, 21, 37)}
	]

def conversationAfterTenMinute():
	say('10분이 지났습니다. 비타민 드셨나요?', volume)
	client_answer = listen()
	if client_answer == 'yes':
		if i['type'] == 'C':
			say('잘하셨어요. 비타민 C는 면역력 증진, 감기 예방, 피부 노화를 방지하는 효능이 있습니다. 좋은 하루되세요.', volume)
		elif i['type'] == 'B':
			say('잘하셨어요. 비타민 B는 몸에 활력을 주고 신진대사를 원할히 하는데 도움을 줍니다. 행복하세요', volume)
	elif client_answer== 'no':
		say('비타민을 먹지 못한 이유를 말씀해주세요.', volume)
		client_answer = listen()
		print(client_answer)
		say('대답이 기록되었습니다.', volume)

def conversation():
	now = datetime.now(timezone('Asia/Seoul'))
	print('last 40 sec...')
	for i in alarmList:
		if now.year == i['date'].year and now.month == i['date'].month and now.day == i['date'].day and  now.hour == i['date'].hour and now.minute == i['date'].minute:
			say('비타민 먹을 시간입니다. 드셨나요?', volume)
			client_answer = listen()
			if client_answer == 'yes':
				if i['type'] == 'C':
					say('잘하셨어요. 비타민 C는 면역력 증진, 감기 예방, 피부 노화를 방지하는 효능이 있습니다. 좋은 하루되세요.', volume)
				elif i['type'] == 'B':
					say('잘하셨어요. 비타민 B는 몸에 활력을 주고 신진대사를 원할히 하는데 도움을 줍니다. 행복하세요', volume)
			elif client_answer == 'no':
				say('비타민을 먹어야합니다. 10분 후에 다시 알려드릴께요.', volume)
				Timer(10, conversationAfterTenMinute).start()
			elif client_answer == 'hello':
				say('안녕하세요 비타입니다.', volume)
			elif client_answer == 'bye':
				saying('종료합니다.', volume)
				exit()

def alarm():
	conversation()
	Timer(40, alarm).start()


print('Vita Start')
alarm()
