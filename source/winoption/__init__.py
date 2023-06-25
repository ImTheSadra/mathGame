from .screenconf import *
from .screenshot import *
from pygame.constants import *
from pygame.event import get

def check(t, d):
	pass

def winWork(event, window:Surface):
	if event.type == KEYDOWN:
		if event.key == K_TAB:
			print("get full screen")
			return getFullScreen()
		elif event.key == K_PRINT:
			print("take screen shot")
			takeScreenShot(window)