from pygame.font import init, Font
init()
from .persian_reshaper import reshape
from bidi import algorithm
from pygame import Surface, Rect
#

int_dic = {
	"0": "۰", "1": "۱", "2": "۲",
	"3": "۳", "4": "۴", "5": "۵",
	"6": "۶", "7": "۷", "8": "۸",
	"9": "۹", "10": "۱۰"
}

class FaFont(Font):
	def FaRender(self, text:str, bold:bool=True,color:tuple=(0,0,0), bg=None):
		try:
			for char in text:
				if char in int_dic:
					text = text.replace(char, int_dic[char])
		except:pass
		display = algorithm.get_display(reshape(u"{0}".format(text)))
		surface = self.render(display, bold, color, bg)
		return surface

class SlowRender:
	width = 0
	height = 0
	def __init__(self, text:str, font:FaFont, color:tuple, bg=None):
		self.text = text
		self.now = 0
		self.font = font
		self.color = color
		self.bg = bg

	def blitEn(self, window:Surface, rect:tuple):
		text = self.font.FaRender(self.text[self.now:], True, self.color)
		self.width = text.get_width()
		self.height = text.get_height()

		window.blit(text, rect)
		if self.now != len(self.text):
			self.now += 1

	def blit(self, window:Surface, rect:tuple, p:float=1):
		txt = self.text[:round(self.now)]
		text = self.font.FaRender(txt, True, self.color, self.bg)
		self.width = text.get_width()
		self.height = text.get_height()

		window.blit(text, rect)
		if round(self.now) != len(self.text):
			self.now += p