import requests

url = 'http://vita.p-e.kr/api'

def createChattingRoom(medicine, userId):
    res = requests.post(url+'/chattingRooms', data={'userId': userId, 'title': 'hhi'})
    return res.json()['newChattingRoom']['id']

def createChattingLog(chattingId, message, talker):
  res = requests.post(url+'/chattingLogs', data={"chattingId":chattingId, "content": message, "talker": talker})
  return res
