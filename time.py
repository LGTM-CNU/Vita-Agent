import time
import threading

def printhello():
	print("hello")
	threading.Timer(5, printhello).start()

printhello()
