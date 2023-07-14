from pygame import (
	image, transform, Rect,
	Surface, quit as pg_quit,
	init
)
from .window import Window
IDIR = "./package/images"
TDIR = "./package/texts"
import json

class Buttons:
	class Mail:
		img = image.load("./package/images/buttons/mail.png")
		def __init__(self):
			self.img = transform.scale(
				self.img,
				(
					self.img.get_width(),
					self.img.get_height()
				)
			)

		def draw(self, window:Surface):
			R = Rect(
				window.get_width()-5-self.img.get_width(),
				window.get_height()-5-self.img.get_height(),
				self.img.get_width(),
				self.img.get_height()
			)
			window.blit(self.img, R)
			return R

	class pause:
		img = image.load(IDIR+"/buttons/pause.png")
		def draw(self, window):
			R = Rect(
				window.get_width()-self.img.get_width()-5,
				5,
				self.img.get_width(),
				self.img.get_height()
			)
			window.blit(self.img, R)
			return R
	class unpause:
		img = image.load(IDIR+"/buttons/unpause.png")
		def draw(self, window):
			R = Rect(
				window.get_width()/2-self.img.get_width()/2,
				window.get_height()/2-self.img.get_height()/2,
				self.img.get_width(),
				self.img.get_height()
			)
			window.blit(
				self.img,
				R
			)
			return R

	class GoHome:
		def __init__(self):
			self.img:Surface = image.load(IDIR+"/buttons/home.png")
			
		def draw(self, window:Surface):
			R = Rect(
				window.get_width()/4-self.img.get_width()/2,
				window.get_height()/2-self.img.get_height()/2,
				self.img.get_width(),
				self.img.get_height()
			)
			window.blit(self.img, R)
			return R

	class Mute:
		def make_image(self):
			with open("./package/db/database.json", "r") as f:
				data = json.load(f)

			self.img = image.load("./package/images/buttons/voice.png")

			if data["music"] != 0:
				self.img = image.load("./package/images/buttons/voice2.png")

		def __init__(self):
			self.make_image()

		def draw(self, window:Surface):
			R = Rect(
				window.get_width()/4*3-self.img.get_width(),
				window.get_height()/2-self.img.get_height()/2,
				self.img.get_width(),
				self.img.get_height()
			)
			window.blit(
				self.img,
				R
			)
			return R

	class info:
		def __init__(self):
			img:Surface = image.load(IDIR+"/buttons/info.png")
			img = transform.scale(
				img,
				(img.get_width()/7,
				img.get_height()/7)
			)
			self.img = img
		def draw(self, window:Window):
			R = Rect(
				window.SIZE[0]-self.img.get_width()-5,
				0,
				self.img.get_width(),
				self.img.get_height()
			)
			window.blit(
				self.img,
				R
			)
			return R

	class Back:
		def __init__(self):
			img = image.load(IDIR+"/buttons/back.png")
			img = transform.rotate(
				img, 180
			)
			img = transform.scale(
				img,
				(
					img.get_width()/8,
					img.get_height()/8
				)
			)
			self.img = img
		def draw(self, window:Window):
			R:Rect = Rect(
				window.SIZE[0]-self.img.get_width()-5,
				self.img.get_height()*4,
				self.img.get_width(),
				self.img.get_height()
			)
			#await window.blit(self.img, R)
			return R

class Texts:
	class Info:
		def __init__(self, win:Window):
			self.img = image.load(TDIR+"/info.png")
			self.img = transform.scale(
				self.img,
				win.SIZE
			)
			self.window = win
		def draw(self, y:int=0):
			R = Rect(
				0,0,
				self.img.get_width(),
				self.img.get_height()
			)
			self.window.blit(self.img, R)
			return R

class Qr:
	def __init__(self, win:Window):
		self.window = win
		self.img = image.load(IDIR+"/qr.png")
		self.img = transform.scale(
			self.img,
			(
				self.img.get_width()*2,
				self.img.get_height()*2
			)
		)

	def draw(self):
		R = Rect(
			5, 5,
			self.img.get_width(),
			self.img.get_width()
		)
		self.window.blit(self.img, R)
		return R
