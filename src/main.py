from threading import Timer, Thread
from datetime import datetime

from conversation.startConversation import startConversation

volume = 0.1

alarmList = [
		{'type': 'B', 'date': datetime(2022, 11, 5, 16, 7)},
		{'type': 'C', 'date': datetime(2022,10,30,16,37)},
		{'type': 'B', 'date': datetime(2022, 10, 27, 21, 37)}
	]

def alarm():
	startConversation(alarmList, volume)
	Timer(40, alarm).start()


print('Vita Start')
alarm()
