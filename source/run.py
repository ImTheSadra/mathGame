from pygame import image
import sys
#from .game import App
#from .home.info import App as Info
from .home import Home
from .window import Window
import pygame as pg
from pygame.font import init
from pygame.event import get as get_ev
from pygame.constants import *
init()

running = False

def work():
	win = Window()
	running = True
	#app = App()
	#info = Info()
	
	home = Home(win)
	while running:
		home.run()
		#await app.run()

def show_error(err:str,**kawars):
	init()
	win = Window()
	font = pg.font.Font(pg.font.get_default_font(), 50)
	txt = font.render(err, True, (10, 3, 8))

	while True:
		win.fill()

		win.blit(
			txt, (
				win.SIZE[0]/2-txt.get_width()/2,
				win.SIZE[1]/2-txt.get_height()/2
			)
		)

		for event in get_ev():
			if event.type == QUIT:
				sys.exit()

		win.update()

def run(**kawars):
	
	if "debug" in kawars:
		if kawars["debug"]:
			try:
				work()
				#loop.close()
			except Exception as err:
				#loop.close()
				if err.args[0] == "display Surface quit":
					sys.exit()
					return
				txt = ""
				for arg in err.args:
					txt += arg
				show_error(err=txt)
		else:
			work()
	else:
		work()