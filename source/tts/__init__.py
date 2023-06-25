import pyttsx3 as tts
from threading import Thread

class TTS:
	def __init__(self):
		self.machine = tts.init()

	def say(self, text:str):
		self.machine.say(text)
		self.machine.runAndWait()

	def threadSay(self, text:str):
		func = Thread(target=self.say, args=[text])
		func.start()

	def getVolume(self):
		return self.machine.getProperty('volume')

	def setVolume(self, v:float):
		self.machine.setProperty('volume', v)