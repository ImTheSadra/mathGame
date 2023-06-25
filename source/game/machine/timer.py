import pygame
from pygame.constants import *

class Timer:
	second = 0
	def __init__(self, maxTime:int):
		self.maxTime = maxTime
		self.event = USEREVENT+1
		pygame.time.set_timer(self.event, 1000)
	
	def step(self, event):
		if event.type == self.event:
			self.second += 1
	
	def check(self):
		return self.second >= self.maxTime

	def getSecond(self):
		return self.maxTime-self.second