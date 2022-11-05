from time import sleep
from multiprocessing import Process

from util.tts import say
from util.speechToText import listen
from util.reponseClassification import classification


def saying(text, volume):
  s = Process(target=(say), args=(text, volume))
  s.start()
  return s

def conversationAfterTenMinute(i, volume):
	say('10분이 지났습니다. 비타민 드셨나요?', volume)
	sleep(2)
	client_answer = listen()
	s.join()
	client_answer = classification(client_answer)
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
