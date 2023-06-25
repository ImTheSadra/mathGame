from pygame import *
from .card import Card
from random import choice
from ...FaFont import init, FaFont
#from ...images import machine_image
import json, os

font = FaFont("./package/fonts/koh-noor.TTF", 75)

#52, 45

class Machine:
	def __init__(self, canij:bool=False):
		self.canij = canij
		bi = os.listdir("./package/images/ntt/skins/")
		self.baseImg = image.load(f"./package/images/ntt/skins/{choice(bi)}")
		self.baseImg = transform.scale(
			self.baseImg,
			(
				250, 383
			)
		)

	def newVallue(self, cards):
		with open("./package/temp", "r") as f:
			data = json.load(f)

		self.soal = image.load("./package/images/ntt/message.png")
		card = choice(cards)
		
		self.img = self.baseImg.copy()
		dcolor = (227, 227, 227)
		self.soal.blit(
			card.display_img,
			(
				9, 30
			)
		)

		self.soal = transform.scale(
			self.soal,
			(
				self.soal.get_width()/3*2,
				self.soal.get_height()/3*2
			)
		)

		data["target"] = card.id
		with open("./package/temp", "w") as f:
			json.dump(data, f)
		return card.id

	def show(self, window:Surface):
		window.blit(
			self.img,
			(
				window.get_width()-self.img.get_width()-self.soal.get_width(),
				window.get_height()-self.img.get_height()
			)
		)
		window.blit(
			self.soal,
			(
				window.get_width()-(self.soal.get_width()*3/2),
				window.get_height()-self.img.get_height()-(self.soal.get_height()*2/3)
			)
		)