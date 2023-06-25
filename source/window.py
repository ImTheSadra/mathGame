from pygame import (
	display, transform, image,
	time, RESIZABLE, Surface
)
from pygame.event import get as get_ev

class Window:
	SIZE = (0,0)
	surface:Surface = Surface((100, 100))
	bg:Surface = Surface((100, 100))
	def __init__(self, SIZE:tuple=(1000, 700)):
		self.SIZE = SIZE
		self.surface = display.set_mode(SIZE, RESIZABLE)
		self.icon = image.load("./package/images/icons/icon.png")
		display.set_icon(self.icon)
		display.set_caption("عملیات رو بردارها")

	def event(self, **kawars):
		return get_ev()

	def fill(self, **kwargs):
		color = (255, 255, 255)
		if "color" in kwargs:
			color = kwargs["color"]

		self.surface.fill(color)
		
		if "background" in kwargs:
			bg = kwargs["background"]
		else:
			bg = self.bg

		bg = transform.scale(
			bg,
			self.SIZE
		)

		pos = (0, 0)
		if "pos" in kwargs:
			pos = kwargs["pos"]

		self.surface.fill(color)
		self.surface.blit(bg, pos)

	def update(self):
		self.SIZE = (
			self.surface.get_width(),
			self.surface.get_height()
		)
		display.update()
		display.flip()
		#print("-")
		clock = time.Clock()
		fps = clock.get_fps()
		if fps == 0:
			fps = 60
		clock.tick(fps)
		

	def blit(self, item:Surface, rect:tuple, **kawars):
		self.surface.blit(item, rect)