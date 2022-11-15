def classification(text):
  if '아니' in text or '안' in text or '먹지않' in text or '먹을' in text:
    return 'no'
  elif '응' in text or '먹었' in text or '어' in text or '네' in text:
    return 'yes'
  elif '비타안녕' in text:
    return 'hello'
  elif '잘가' in text:
    return 'bye'
  elif '테스트' in text:
    print('테스트')
    return 'etc'
  else:
    return 'etc'