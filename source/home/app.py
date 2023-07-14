from ..window import Window
from ..images import *
from ..game import Game
import os, json
from random import choice
from pygame import (
	image, mouse, display, mixer, draw
)
from pygame.event import get as get_ev
from pygame.constants import *
import pygame as pg
from .info import Info
from ..FaFont import FaFont
from ..winoption import check
from datetime import datetime
import webbrowser
from ..chat import App as Chat

font = FaFont("./package/fonts/Noto.ttf", 30)
smallFont = font = FaFont("./package/fonts/Noto.ttf", 18)

def getWeb():
	#webbrowser.open("index.html")
	pass

with open("./package/db/database.json", "r") as f:
	data = json.load(f)

class Home:
	running = True
	with open("./package/db/database.json", "r") as f:
		data = json.load(f)

	def play(self):
		mixer.init()
		mixer.music.load("./package/sounds/homeBg.mp3")
		mixer.music.play(loops=100)
		bg_y = self.window.SIZE[1]
		oSize = self.window.SIZE
		lock_img = image.load("./package/images/icons/lock.png")
		unlock_img = image.load("./package/images/icons/unlock.png")
		lock_icon = image.load("./package/images/buttons/lock.png")
		lock_icon = transform.scale(
			lock_icon,
			(
				30,30
			)
		)
		self.music_pos = 11
		chatBtn = Buttons.Mail()
		aboutWeBtn = image.load("./package/images/buttons/info.png")
		aboutWeBtn = pg.transform.scale(
			aboutWeBtn,
			(
				aboutWeBtn.get_width()/5,
				aboutWeBtn.get_height()/5
			)
		)
		aboutWeY = 0
		p = -1
		while self.running:

			self.window.fill()

			bg = transform.scale(
				self.bg,
				(
					self.window.SIZE[0],
					self.window.SIZE[1]
				)
			)

			self.window.blit(bg, (0,0))

			info = Rect(
				self.window.SIZE[0]-aboutWeBtn.get_width(), aboutWeY,
				aboutWeBtn.get_width(), aboutWeBtn.get_height()
			)

			self.window.blit(aboutWeBtn, info)

			if info.collidepoint(mouse.get_pos()):
				if aboutWeY <= -20:
					p = 1
				if aboutWeY >= 0:
					p = -1
				aboutWeY += p
			else:aboutWeY = 0


			chatBtnR = chatBtn.draw(self.window.surface)

			if chatBtnR.collidepoint(mouse.get_pos()):
				txt = smallFont.FaRender("پیام رسان!", True, (255,255,255), (144, 66, 245))
				self.window.blit(
					txt,
					(
						chatBtnR.x-(txt.get_width()/2),
						chatBtnR.y-txt.get_height()-5
					)
				)

			#level 1
			self.img = unlock_img.copy()
			
			level1 = self.data["levels"][0]
			level1Rect = Rect(
				self.window.SIZE[0]/6-self.img.get_width(),
				self.window.SIZE[1]/2-self.img.get_height(),
				self.img.get_width(),
				self.img.get_height()
			)

			if level1["lock"]:
				self.img = lock_img.copy()
				self.img.blit(
					lock_icon,
					(
						-5,0
					)
				)
			#print(level1["lock"])

			text = font.FaRender("1", True, (255,255,255))
			self.img.blit(
				text,
				(
					self.img.get_width()/2-text.get_width()/2,
					self.img.get_height()/2-text.get_height()/2
				)
			)

			if level1Rect.collidepoint(mouse.get_pos()):
				self.img.set_alpha(200)

			self.window.blit(
				self.img,
				level1Rect
			)

			#level 2
			self.img = unlock_img.copy()

			level2 = self.data["levels"][1]
			level2Rect = Rect(
				self.window.SIZE[0]/6*2-self.img.get_width(),
				self.window.SIZE[1]/2-self.img.get_height(),
				self.img.get_width(),
				self.img.get_height()
			)

			if level2["lock"]:
				self.img = lock_img.copy()
				self.img.blit(
					lock_icon,
					(
						-5,0
					)
				)
			#print(level2["lock"])

			text = font.FaRender("2", True, (255,255,255))
			self.img.blit(
				text,
				(
					self.img.get_width()/2-text.get_width()/2,
					self.img.get_height()/2-text.get_height()/2
				)
			)

			if level2Rect.collidepoint(mouse.get_pos()):
				self.img.set_alpha(200)

			self.window.blit(
				self.img,
				level2Rect
			)

			#level 3

			self.img = unlock_img.copy()

			level3 = self.data["levels"][2]
			level3Rect = Rect(
				self.window.SIZE[0]/6*3-self.img.get_width(),
				self.window.SIZE[1]/2-self.img.get_height(),
				self.img.get_width(),
				self.img.get_height()
			)

			if level3["lock"]:
				self.img = lock_img.copy()
				self.img.blit(
					lock_icon,
					(
						-5,0
					)
				)
			#print(level3["lock"])

			text = font.FaRender("3", True, (255,255,255))
			self.img.blit(
				text,
				(
					self.img.get_width()/2-text.get_width()/2,
					self.img.get_height()/2-text.get_height()/2
				)
			)

			if level3Rect.collidepoint(mouse.get_pos()):
				self.img.set_alpha(200)

			self.window.blit(
				self.img,
				level3Rect
			)

			#level 4

			self.img = unlock_img.copy()

			level4 = self.data["levels"][3]
			level4Rect = Rect(
				self.window.SIZE[0]/6*4-self.img.get_width(),
				self.window.SIZE[1]/2-self.img.get_height(),
				self.img.get_width(),
				self.img.get_height()
			)

			if level4["lock"]:
				self.img = lock_img.copy()
				self.img.blit(
					lock_icon,
					(
						-5,0
					)
				)
			#print(level3["lock"])

			text = font.FaRender("4", True, (255,255,255))
			self.img.blit(
				text,
				(
					self.img.get_width()/2-text.get_width()/2,
					self.img.get_height()/2-text.get_height()/2
				)
			)

			if level4Rect.collidepoint(mouse.get_pos()):
				self.img.set_alpha(200)

			self.window.blit(
				self.img,
				level4Rect
			)

			draw.rect(
				self.window.surface,
				(63, 21, 130),
				(
					2, 
					self.window.SIZE[1]-self.place_name.get_height()-5, 
					self.place_name.get_width()+5,
					self.place_name.get_height()-5
				), 0,
				15
			)
			self.window.blit(self.place_name, 
				(
					5,
					self.window.SIZE[1]-self.place_name.get_height()-10
				)
			)

			#level 5
			self.img = unlock_img.copy()

			level5 = self.data["levels"][4]
			level5Rect = Rect(
				self.window.SIZE[0]/6*5-self.img.get_width(),
				self.window.SIZE[1]/2-self.img.get_height(),
				self.img.get_width(),
				self.img.get_height()
			)

			if level5["lock"]:
				self.img = lock_img.copy()
				self.img.blit(
					lock_icon,
					(
						-5,0
					)
				)
			#print(level2["lock"])

			text = font.FaRender("5", True, (255,255,255))
			self.img.blit(
				text,
				(
					self.img.get_width()/2-text.get_width()/2,
					self.img.get_height()/2-text.get_height()/2
				)
			)

			if level5Rect.collidepoint(mouse.get_pos()):
				self.img.set_alpha(200)

			self.window.blit(
				self.img,
				level5Rect
			)

			qr = Qr(self.window)
			qr = qr.draw()

			oclick = None

			if qr.collidepoint(mouse.get_pos()):
				txt = smallFont.FaRender("اسکن کنید!", True, (255,255,255), (144, 66, 245))
				r = (
					qr.x+20,
					qr.y+5+qr.h
				)
				self.window.blit(txt, r)


			for event in get_ev():
				if event.type == QUIT:pg.quit()
				elif event.type == KEYDOWN:
					if event.key == K_TAB:
						pass
				elif event.type == MOUSEBUTTONDOWN:
					if event.button in [1, 3]:
						oclick = event.pos
						if qr.collidepoint(event.pos):
							getWeb()
						if info.collidepoint(event.pos):
							app = Info(self.window)
							app.run(background=self.bg)

						c = check(event, self.window.surface)
						if c != None:
							self.window.surface = c

						if not level1["lock"]:
							if level1Rect.collidepoint(oclick):
								mixer.music.stop()
								mouse.set_cursor(SYSTEM_CURSOR_WAITARROW)
								game = Game(0, music=self.music_pos)
								game.run()
								self.music_pos = game.music_pos
								display.set_caption("عملیات رو بردارها")
								mouse.set_cursor(SYSTEM_CURSOR_ARROW)
								with open("./package/db/database.json", "r") as f:
									self.data = json.load(f)
								mixer.music.load("./package/sounds/homeBg.mp3")
								mixer.music.play(loops=100)
								self.bgn = choice(
									os.listdir("./package/images/backgrounds/home/")
								)
								self.bg = image.load("./package/images/backgrounds/home/"+self.bgn)
								self.place_name = font.FaRender(
								self.bgn.replace(".jpg", ""),
									True,
									(255,255,255)
								)

						if not level2["lock"]:
							if level2Rect.collidepoint(oclick):
								mixer.music.stop()
								mouse.set_cursor(SYSTEM_CURSOR_WAITARROW)
								game = Game(1, music=self.music_pos)
								game.run()
								self.music_pos = game.music_pos
								mouse.set_cursor(SYSTEM_CURSOR_ARROW)
								display.set_caption("عملیات رو بردارها")
								with open("./package/db/database.json", "r") as f:
									self.data = json.load(f)
								mixer.music.load("./package/sounds/homeBg.mp3")
								mixer.music.play(loops=100)
								self.bgn = choice(
									os.listdir("./package/images/backgrounds/home/")
								)
								self.bg = image.load("./package/images/backgrounds/home/"+self.bgn)
								self.place_name = font.FaRender(
								self.bgn.replace(".jpg", ""),
									True,
									(255,255,255)
								)

						if not level3["lock"]:
							if level3Rect.collidepoint(oclick):
								mixer.music.stop()
								mouse.set_cursor(SYSTEM_CURSOR_WAITARROW)
								game = Game(2, music=self.music_pos)
								game.run()
								self.music_pos = game.music_pos
								display.set_caption("عملیات رو بردارها")
								mouse.set_cursor(SYSTEM_CURSOR_ARROW)
								with open("./package/db/database.json", "r") as f:
									self.data = json.load(f)
								mixer.music.load("./package/sounds/homeBg.mp3")
								mixer.music.play(loops=100)
								self.bgn = choice(
									os.listdir("./package/images/backgrounds/home/")
								)
								self.bg = image.load("./package/images/backgrounds/home/"+self.bgn)
								self.place_name = font.FaRender(
								self.bgn.replace(".jpg", ""),
									True,
									(255,255,255)
								)

						if not level4["lock"]:
							if level4Rect.collidepoint(oclick):
								mixer.music.stop()
								mouse.set_cursor(SYSTEM_CURSOR_WAITARROW)
								game = Game(3, music=self.music_pos)
								game.run()
								self.music_pos = game.music_pos
								display.set_caption("عملیات رو بردارها")
								mouse.set_cursor(SYSTEM_CURSOR_ARROW)
								with open("./package/db/database.json", "r") as f:
									self.data = json.load(f)
								mixer.music.load("./package/sounds/homeBg.mp3")
								mixer.music.play(loops=100)
								self.bgn = choice(
									os.listdir("./package/images/backgrounds/home/")
								)
								self.bg = image.load("./package/images/backgrounds/home/"+self.bgn)
								self.place_name = font.FaRender(
								self.bgn.replace(".jpg", ""),
									True,
									(255,255,255)
								)

						if not level5["lock"]:
							if level5Rect.collidepoint(oclick):
								mixer.music.stop()
								mouse.set_cursor(SYSTEM_CURSOR_WAITARROW)
								game = Game(4, music=self.music_pos)
								game.run()
								self.music_pos = game.music_pos
								display.set_caption("عملیات رو بردارها")
								mouse.set_cursor(SYSTEM_CURSOR_ARROW)
								with open("./package/db/database.json", "r") as f:
									self.data = json.load(f)
								mixer.music.load("./package/sounds/homeBg.mp3")
								mixer.music.play(loops=100)
								self.bgn = choice(
									os.listdir("./package/images/backgrounds/home/")
								)
								self.bg = image.load("./package/images/backgrounds/home/"+self.bgn)
								self.place_name = font.FaRender(
								self.bgn.replace(".jpg", ""),
									True,
									(255,255,255)
								)

						if chatBtnR.collidepoint(event.pos):
							app = Chat(self.window.surface)
							app.chatting()

			self.window.update()
			oSize = self.window.SIZE

	def run(self):
		self.play()

	def __init__(self, win:Window):
		self.window = win
		self.bgn = choice(
			os.listdir("./package/images/backgrounds/home/")
		)
		self.bg = image.load("./package/images/backgrounds/home/"+self.bgn)
		self.place_name = font.FaRender(
			self.bgn.replace(".jpg", ""),
			True,
			(255,255,255)
		)
		with open("./package/temp2", "r") as f:
			data2 = json.load(f)

		data2["music_pos"] = 11

		with open("./package/temp2", "w") as f:
		    json.dump(data2, f)