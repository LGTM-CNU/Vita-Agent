from threading import Timer
from multiprocessing import Process
from time import sleep

from util.tts import say
from util.speechToText import listen
from util.chatService import createChattingRoom, createChattingLog
from conversation.afterTenMinuteConversation import conversationAfterTenMinute
from util.reponseClassification import classification
from util.medicineService import checkMedicines

def saying(text, volume, chattingRoomId):
  s = Process(target=(say), args=(text, volume))
  s.start()
  createChattingLog(chattingRoomId, text, 'vita')
  return s

def startConversation(medicines, volume, userId):
  print('last 40 sec...')
  for medicine in medicines:
    if checkMedicines(medicine):
      chattingRoomId = createChattingRoom('123', userId) # Test
      s = saying('영균아 비타민 먹을 시간인데 먹었어?', volume, chattingRoomId)
      sleep(2)
      client_answer = listen()
      s.join()
      createChattingLog(chattingRoomId, client_answer, userId)
      client_answer = classification(client_answer)
      if client_answer == 'yes':
        if 'C' in medicine['medicines_type']:
          saying('잘하셨어요. 비타민 C는 면역력 증진, 감기 예방, 피부 노화를 방지하는 효능이 있습니다. 좋은 하루되세요.', volume, chattingRoomId)
        elif 'B' in medicine['medicines_type']:
          saying('잘하셨어요, . 비타민 B는 몸에 활력을 주고 신진대사를 원할히 하는데 도움을 줍니다. 행복하세요', volume, chattingRoomId)
        else:
          saying('건강하세요.',volume, chattingRoomId)
      elif client_answer == 'no':
        saying('3분후에 다시 물어보러 올께.', volume, chattingRoomId)
        Timer(180, conversationAfterTenMinute, [medicines, volume, chattingRoomId, userId]).start()
      elif client_answer == 'hello':
        saying('안녕하세요 비타입니다.', volume, chattingRoomId)
      elif client_answer == 'bye':
        saying('종료합니다.', volume, chattingRoomId)
        exit()
