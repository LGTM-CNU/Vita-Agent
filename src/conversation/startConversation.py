from datetime import datetime
from pytz import timezone
from threading import Timer
from multiprocessing import Process
from time import sleep

from util.tts import say
from util.speechToText import listen
from conversation.afterTenMinuteConversation import conversationAfterTenMinute
from util.reponseClassification import classification

def saying(text, volume):
  s = Process(target=(say), args=(text, volume))
  s.start()
  return s

def startConversation(alarmList, volume):
  now = datetime.now(timezone('Asia/Seoul'))
  print('last 40 sec...')
  for i in alarmList:
    if now.year == i['date'].year and now.month == i['date'].month and now.day == i['date'].day and  now.hour == i['date'].hour and now.minute == i['date'].minute:
      s = saying('비타민 먹을 시간입니다. 드셨나요?', volume)
      sleep(2)
      client_answer = listen()
      s.join()
      client_answer = classification(client_answer)
      if client_answer == 'yes':
        if i['type'] == 'C':
          saying('잘하셨어요. 비타민 C는 면역력 증진, 감기 예방, 피부 노화를 방지하는 효능이 있습니다. 좋은 하루되세요.', volume)
        elif i['type'] == 'B':
          saying('잘하셨어요. 비타민 B는 몸에 활력을 주고 신진대사를 원할히 하는데 도움을 줍니다. 행복하세요', volume)
      elif client_answer == 'no':
        saying('비타민을 먹어야합니다. 10분 후에 다시 알려드릴께요.', volume)
        Timer(10, conversationAfterTenMinute, [i, volume]).start()
      elif client_answer == 'hello':
        saying('안녕하세요 비타입니다.', volume)
      elif client_answer == 'bye':
        saying('종료합니다.', volume)
        exit()
