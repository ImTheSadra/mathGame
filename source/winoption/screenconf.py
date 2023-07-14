from pygame import display, FULLSCREEN

def getFullScreen():
	window = display.set_mode((0,0), FULLSCREEN)
	return window