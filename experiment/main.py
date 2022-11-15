from threading import Timer, Thread
from datetime import datetime

from conversation.startConversation import startConversation

from util.medicineService import getMedicinesList

volume = 0.1
userId = '12'

def alarm():
	medicineList = getMedicinesList(userId)
	print(medicineList)

	startConversation(medicineList, volume, userId)
	Timer(59, alarm).start()


print('Vita Start')
alarm()
