from pygame import *
from random import choice
init()
from ...FaFont import FaFont, init
init()
font = FaFont("./package/fonts/fa.ttf", 40)
font2 = FaFont("./package/fonts/fa.ttf", 55)
import json

#nRange = range(-10, 11)

def a_number():
	return choice(range(-10, 11))

def t(v1:tuple, v2:tuple, n1:int, n2:int):
	result = (
		(n1)*(v1[0])+n2*(v2[0]),
		(n1)*(v1[1])+n2*(v2[1])
	)
	return result

def d(v1:tuple, v2:tuple, n1:int, n2:int):
	result = (
		n1*(v1[0])-n2*(v2[0]),
		n1*(v1[1])-n2*(v2[1])
	)
	return result

def x(v:tuple, n:int):
	return (
		n*v[0],
		n*v[1]
	)

opr_functions = {
	"+": t,
	"-": d,
	"*": x
}

rects = {
	"n": Rect(46, 30, 0, 0),
	"t1": Rect(99, 5, 0, 0),
	"t2": Rect(99, 40, 0, 0),
	"n1": Rect(3, 30, 0, 0),
	"t11": Rect(45, 10, 0, 0),
	"t12": Rect(45, 45, 0, 0),
	"n2": Rect(133, 30, 0, 0),
	"t21": Rect(180, 10, 0, 0),
	"t22": Rect(180, 45, 0, 0),
	"opr": Rect(110, 30, 0, 0)
}

with open("./package/temp", "w") as f:
	json.dump({"cid": 0}, f)

with open("./package/temp", "r") as f:
	data = json.load(f)

class Card:
	def __init__(self, rect:Rect, oprs:list=["+"], cans=False):
		data["cid"] += 1
		self.id = data["cid"]
		with open("./package/temp", "w") as f:
			json.dump(
				data,
				f
			)
		self.rect:Rect = rect
		self.opr = choice(oprs)
		x = ""
		if self.opr == "*": x="x"
		if self.opr == "ij": x="n"

		dcolor = (255, 255, 255)

		if "ij" in oprs and "*" in oprs or "ij" in oprs and cans:
			self.value1 = (a_number(), a_number())
			self.value2 = (a_number(), a_number())

			self.vallue = (
				self.value1[0]+self.value2[0],
				self.value1[1]+self.value2[1]
			)

			self.makeImg([(190, 5)])

			t = "+"
			if self.value1[1] <= -1:
				t = " "

			text = "({0}i{2}{1}j) + ".format(
				str(self.value1[0]), str(self.value1[1]), t
			)

			text = font.FaRender(
				text, True, dcolor
			)
			v1 = font.FaRender(
				str(self.value2[0]), True, dcolor
			)
			v2 = font.FaRender(
				str(self.value2[1]), True, dcolor
			)

			self.display_img.blit(
				v1,
				(200, 8)
			)
			self.display_img.blit(
				v2,
				(200, v2.get_height())
			)


			self.display_img.blit(
				text,
				(
					self.display_img.get_width()/3-text.get_width()/3-10,
					self.display_img.get_height()/2-text.get_height()/2
				)
			)

			return

		if self.opr == "ij":
			self.value = (a_number(), a_number())
			self.vallue = self.value

			self.makeImg()

			value = self.value

			t = "+"
			if self.value[1] <= -1:
				t = " "

			i = str(self.value[0])+"i"
			if i == "0i":
				i = ""
			elif i == "1i":
				i = "i"
			j = str(self.value[1])+"j"
			if j == "0j":
				j = ""
			elif j == "1j":
				j = "j"
			text = f"{i} {t} {j}"
			text = font2.FaRender(
				text, True, (255,255,255)
			)

			self.display_img.blit(
				text,
				(
					self.display_img.get_width()/2-text.get_width()/2,
					self.display_img.get_height()/2-text.get_height()/2
				)
			)

			return

		if self.opr == "*":
			if cans:
				self.n = choice(range(1,11))
			else:
				self.n = 1
			self.value = (a_number(), a_number())
			self.vallue = opr_functions[self.opr](self.value, self.n)
			dcolor = (255, 255, 255)
			if cans:
				n = font.FaRender(str(self.n), True, dcolor)

			self.makeImg([(95, 8)])

			t = str(self.value[0])
			if len(t) == 1:
				t = f"  {t}"
			if len(t) == 2:
				t = f" {t}"
			t1 = font.FaRender(t, True, dcolor)
			t = str(self.value[1])
			if len(t) == 1:
				t = f"  {t}"
			if len(t) == 2:
				t = f" {t}"
			t2 = font.FaRender(t, True, dcolor)

			if cans:
				self.display_img.blit(
					n, rects["n"]
				)
			self.display_img.blit(t1, rects["t1"])
			self.display_img.blit(t2, rects["t2"])
			return


		if cans:
			self.n1 = choice(range(1,11))
			self.n2 = choice(range(1,11))
		else:
			self.n1 = 1
			self.n2 = 1

		self.value1 = (a_number(), a_number())
		self.value2 = (a_number(), a_number())
		self.vallue = opr_functions[self.opr](
			self.value1, self.value2,
			self.n1, self.n2
		)

		self.makeImg([(30, 9), (171, 9)])

		dcolor = (255, 255, 255)

		if cans:
			n1 = font.FaRender(str(self.n1), True, dcolor)
			n2 = font.FaRender(" "+str(self.n2), True, dcolor)
		t = str(self.value1[0])
		if len(t) == 1:
			t = f"  {t}"
		if len(t) == 2:
			t = f" {t}"
		t11 = font.FaRender(t, True, dcolor)
		t = str(self.value1[1])
		if len(t) == 1:
			t = f"  {t}"
		if len(t) == 2:
			t = f" {t}"
		t12 = font.FaRender(t, True, dcolor)
		t = str(self.value2[0])
		if len(t) == 1:
			t = f"  {t}"
		if len(t) == 2:
			t = f" {t}"
		t21 = font.FaRender(t, True, dcolor)
		t = str(self.value2[1])
		if len(t) == 1:
			t = f"  {t}"
		if len(t) == 2:
			t = f" {t}"
		t22 = font.FaRender(t, True, dcolor)
		if not cans:
			self.opr = f" {self.opr}"
		opr = font.FaRender(" "+str(self.opr), True, dcolor)

		if cans:
			self.display_img.blit(n1, rects["n1"])
			self.display_img.blit(n2, rects["n2"])
		self.display_img.blit(t11, rects["t11"])
		self.display_img.blit(t12, rects["t12"])
		self.display_img.blit(t21, rects["t21"])
		self.display_img.blit(t22, rects["t22"])
		self.display_img.blit(opr, rects["opr"])

		self.img = image.load("./package/images/card_img.png")
		v1 = font.FaRender(
			str(self.vallue[0]), True, dcolor
		)
		v2 = font.FaRender(
			str(self.vallue[1]), True, dcolor
		)

		self.img.blit(
			v2, (
				self.img.get_width()/2-v2.get_width()/2,
				self.img.get_height()/2-v2.get_height()/3/3*2
			)
		)
		self.img.blit(
			v1, (
				self.img.get_width()/2-v1.get_width()/2,
				5
			)
		)

	def makeImg(self, ks:list=[]):
		dcolor = (255, 255, 255)
		k = image.load("./package/images/card.png")
		self.display_img = Surface((280, 120))
		self.display_img.fill((18,85,169))
		for i in ks:
			self.display_img.blit(
				k, i
			)
		self.img = image.load(".\\package\\images\\card_img.png")
		v1 = font.FaRender(
			str(self.vallue[0]), True, dcolor
		)
		v2 = font.FaRender(
			str(self.vallue[1]), True, dcolor
		)

		self.img.blit(
			v2, (
				self.img.get_width()/2-v2.get_width()/2,
				self.img.get_height()/2-10
			)
		)
		self.img.blit(
			v1, (
				self.img.get_width()/2-v1.get_width()/2,
				0
			)
		)
		self.IMG = image.load("./package/images/card.png")
		self.IMG = transform.scale(
			self.IMG,
			(
				self.img.get_width()+4,
				self.img.get_height()+4
			)
		)
		self.IMG.blit(
			self.img,
			(
				self.IMG.get_width()/2-self.img.get_width()/2,
				self.IMG.get_height()/2-self.img.get_height()/2
			)
		)

	def show(self, window:Surface, fill:tuple=None):
		if fill != None:
			dcolor = (255, 255, 255)
			self.img = image.load(".\\package\\images\\card_img.png")
			fill_rect = self.rect.copy()
			fill_rect.x = 0
			fill_rect.y = 0
			draw.rect(
				self.img,
				fill,
				fill_rect,
				0,
				11
			)
			v1 = font.FaRender(
				str(self.vallue[0]), True, dcolor
			)
			v2 = font.FaRender(
				str(self.vallue[1]), True, dcolor
			)

			self.img.blit(
				v2, (
					self.img.get_width()/2-v2.get_width()/2,
					self.img.get_height()/2-10
				)
			)
			self.img.blit(
				v1, (
					self.img.get_width()/2-v1.get_width()/2,
					0
				)
			)
			self.IMG = image.load("./package/images/card.png")
			self.IMG = transform.scale(
				self.IMG,
				(
					self.img.get_width()+4,
					self.img.get_height()+4
				)
			)
			self.IMG.blit(
				self.img,
				(
					self.IMG.get_width()/2-self.img.get_width()/2,
					self.IMG.get_height()/2-self.img.get_height()/2
				)
			)

		self.img = transform.scale(
			self.img, (self.rect.w, self.rect.h)
		)

		window.blit(
			self.img,
			self.rect
		)