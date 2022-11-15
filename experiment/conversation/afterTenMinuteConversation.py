from time import sleep
from multiprocessing import Process

from util.tts import say
from util.speechToText import listen
from util.reponseClassification import classification
from util.chatService import createChattingRoom, createChattingLog

def saying(text, volume, chattingId):
  s = Process(target=(say), args=(text, volume))
  s.start()
  createChattingLog(chattingId, text, 'vita')
  return s

def conversationAfterTenMinute(i, volume, chattingId, userId):
	s = saying('소영이누나, 3분 지났는데 비타민 먹었어?', volume, chattingId)
	sleep(2)
	client_answer = listen()
	s.join()
	createChattingLog(chattingId, client_answer, userId)
	client_answer = classification(client_answer)
	if client_answer == 'yes':
		if i['medicines_type'] == 'C':
			saying('잘하셨어요. 비타민 C는 면역력 증진, 감기 예방, 피부 노화를 방지하는 효능이 있습니다. 좋은 하루되세요.', volume, chattingId)
		elif i['medicines_type'] == 'B':
			saying('잘하셨어요. 비타민 B는 몸에 활력을 주고 신진대사를 원할히 하는데 도움을 줍니다. 행복하세요', volume, chattingId)
		else:
			saying('잘하셨어요. 비타민은 몸에 좋습니다. 행복하세요', volume, chattingId)
	elif client_answer== 'no':
		s = saying('비타민을 먹지 못한 이유를 말씀해주세요.', volume, chattingId)
		sleep(2)
		client_answer = listen()
		print(client_answer)
		s.join()
		createChattingLog(chattingId, client_answer, userId)
		saying('대답이 기록되었습니다.', volume, chattingId)
