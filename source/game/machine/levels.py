import json
from pygame import Surface, Rect, image, display
from .card import Card
from .timer import Timer
from .machine import Machine
from PIL import Image

class LevelsMachine:
	def __init__(self, level:int=1):
		with open("./package/db/database.json", "r") as f:
			self.data = json.load(f)
		self.level = self.data["levels"][level]
		display.set_caption("عملیات رو بردارها - {0}".format(self.level["name"]))

	def getBackground(self):
		self.bg = Image.open(
			self.level["background"]
		)
		return self.bg

	def makeCards(self, window:Surface):
		cards = []

		ox = window.get_width()/20
		oy = window.get_height()/20*5
		frameSize = ((window.get_width()*self.level["frameSize"])/1217)-10
		#print(frameSize)
		max_ = window.get_width()/3*2
		width, height = (
			window.get_width()*200/1217,
			window.get_height()*116/746
		)
		#print(width, height)
		for i in range(self.level["maxCards"]):
			rect = Rect(ox, oy, width, height)
			card = Card(rect, self.level["oprs"], self.level["can*"])
			cards.append(card)
			ox += card.display_img.get_width()+frameSize
			if ox >= window.get_width()/2:
				ox = window.get_width()/20
				oy += card.display_img.get_height()+frameSize

		return cards

	def makeMachine(self):

		result = Machine(self.level["canij"])

		return result

	def makeTimer(self):
		timer = Timer(self.level["maxTime"])
		return timer