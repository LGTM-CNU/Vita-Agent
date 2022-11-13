import requests
from datetime import datetime
from pytz import timezone

# [{'medicines_id': 'e4a6ab6a-55e1-d640-d46b-78fbdd497bb6',
# 'medicines_morning': '07:00', 'medicines_evening': None, 'medicines_afternoon': None,
# 'medicines_description': '2', 'medicines_type': '1',
# 'medicines_thumbnail': 'medicine1.png', 'medicines_repeat': 24, 'medicines_ownerId': '123'}]

url = 'http://vita.p-e.kr/api'

def getMedicinesList(userId):
  res = requests.get(url+'/medicines/'+userId)
  return res.json()['data']

def checkMedicines(medicine):
  repeat = ("0000000"+str(bin(medicine['medicines_repeat']))[2:])[-7:]
  today = datetime.now(timezone('Asia/Seoul'))
  if medicine['medicines_morning'] != None:
    [hour, minute] = map(int, medicine['medicines_morning'].split(':'))
    if hour == today.hour and today.minute == minute and int(repeat[today.weekday()]): return True
  if medicine['medicines_evening'] != None:
    [hour, minute] = map(int, medicine['medicines_evening'].split(':'))
    if hour == today.hour and today.minute == minute and int(repeat[today.weekday()]): return True
  if medicine['medicines_afternoon'] != None:
    [hour, minute] = map(int, medicine['medicines_afternoon'].split(':'))
    if hour == today.hour and today.minute == minute and int(repeat[today.weekday()]): return True
  return False