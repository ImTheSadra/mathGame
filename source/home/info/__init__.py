from pygame.event import get as get_ev
from pygame.constants import *
from ...window import Window
from pygame import draw, mouse
import pygame as pg
from ...images import *

class Info:
	def __init__(self, win:Window):
		self.win = win

	def play(self, **kwargs):
		running = True
		
		while running:
			
			self.win.fill(**kwargs)
			
			info = Texts.Info(self.win)
			info = info.draw()

			back = Buttons.Back()
			back = back.draw(self.win)

			for event in get_ev():
				if event.type == QUIT:pg.quit()
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:running=False
				#elif event.type == MOUSEBUTTONDOWN:
					#if event.button in [1, 3]:
					#	if back.collidepoint(event.pos):running=False

			self.win.update()

	def run(self, **kwargs):
		self.play(**kwargs)