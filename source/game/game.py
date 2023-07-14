from ..window import Window
from pygame.event import get as get_ev
from ..FaFont import FaFont, SlowRender
from .machine import *
from pygame import *
import sys, json, os, asyncio, time as time2
from ..images import Buttons
from random import choice
from ..winoption import *
from PIL import Image
from io import BytesIO

level_c = range(17,0,-1)

font = FaFont("./package/fonts/koh-noor.TTF", 40)

class Game:
	qatar = Image.open("./package/images/backgrounds/game/qatar.gif")
	pilBg = None
	bgN = 0
	qN = 0
	game_play_ = False
	game_over_ = False
	game_winn_ = False
	game_start = True
	running = False
	defult_size = (1280, 706)
	music_pos = 11
	def __init__(self, level:int, **kwargs):
		self.running = True
		self.window = display.set_mode((1280, 706), HWSURFACE|DOUBLEBUF|RESIZABLE)
		self.level = level
		self.fullscreen = False
		if "music" in kwargs:
			self.music_pos = kwargs["music"]

	def newValue(self):
		self.vallue

	def blitBg(self):
		self.window.fill((0, 0, 0))

		try:
			if self.bgN >= self.pilBg.n_frames:
				self.bgN = 0
			self.pilBg.seek(self.bgN)
		except:pass
		data = BytesIO()
		self.pilBg.save(data, format="PNG")
		data.seek(0)
		bg = image.load(data)

		bg = transform.scale(
			bg,
			(self.window.get_width(), self.window.get_height())
		)

		self.window.blit(bg, (0,0))
		self.bgN += 1

	def blitQatar(self):
		self.window.fill((0, 0, 0))

		try:		
			if self.qN >= self.qatar.n_frames:
				self.qN = 0
			self.qatar.seek(self.qN)
		except:pass
		data = BytesIO()
		self.qatar.save(data, format="PNG")
		data.seek(0)
		bg = image.load(data)

		bg = transform.scale(
			bg,
			(self.window.get_width(), self.window.get_height())
		)

		self.window.blit(bg, (0,0))
		self.qN += 1

	def starting(self):
		if not self.game_start:
			return

		mouse.set_cursor(SYSTEM_CURSOR_ARROW)

		nFont = FaFont("./package/fonts/koh-noor.TTF", 180)

		mixer.init()
		mixer.music.load("./package/sounds/start.mp3")
		mixer.music.play()
		timer = Timer(3)

		while self.game_start:
			self.window.fill((255,255,255))

			text = nFont.FaRender(
				str(timer.getSecond()),
				True, (0,0,0)
			)

			self.window.blit(
				text,
				(
					self.window.get_width()/2-text.get_width()/2,
					self.window.get_height()/2-text.get_height()/2
				)
			)

			for event in get_ev():
				if event.type == QUIT:sys.exit()
				timer.step(event)
				c = check(event, self.window)
				if c != None:
					self.window = c

			if timer.second == 4:
				self.game_start = False
				self.game_play_ = True
				mouse.set_cursor(SYSTEM_CURSOR_WAITARROW)

			display.update()

	def pause(self):

		bg = self.window.copy()
		bg.set_alpha(60)
		paused = True
		btn = Buttons.unpause()
		home_btn = Buttons.GoHome()
		music_btn = Buttons.Mute()
		while paused:
			self.music_pos = mixer.music.get_pos()/100000
			self.window.fill((0,0,0))
			bg = transform.scale(
				bg,
				(
					self.window.get_width(),
					self.window.get_height()
				)
			)
			self.window.blit(bg, (0,0))
			for i in range(3):
				rect = btn.draw(self.window)
				
				goHome = home_btn.draw(self.window)
				
				musicBtn = music_btn.draw(self.window)
			

			if rect.collidepoint(mouse.get_pos()) or goHome.collidepoint(mouse.get_pos()):
				mouse.set_cursor(SYSTEM_CURSOR_HAND)
			else:
				mouse.set_cursor(SYSTEM_CURSOR_ARROW)

			if mouse.get_pressed()[0]:
				if rect.collidepoint(mouse.get_pos()):
					paused = False
					mouse.set_cursor(SYSTEM_CURSOR_ARROW)
				elif goHome.collidepoint(mouse.get_pos()):
					paused = False
					mixer.music.stop()
					mixer.music.unload()
					self.running = False
					self.game_play_ = False
					self.game_over_ = False
					self.game_winn_ = False
					self.game_start = False

			for event in get_ev():
				if event.type == QUIT:sys.exit()
				if event.type == KEYDOWN:
					#print(str(event.key))
					if str(event.key) in ["1073741894"]:
						dirc = os.path.expanduser('~')+"\\Pictures\\عملیات رو بردارها\\"
						path = dirc+"{0}.jpg"
						now = datetime.now()
						image.save(self.window, path.format(str(now)))
					if event.key == K_TAB:
						if self.fullscreen:
							self.window = display.set_mode(
								(
									self.window.get_width(),
									self.window.get_height()
								), RESIZABLE
							)
							self.fullscreen = False
						else:
							self.window = display.set_mode(
								(0,0), FULLSCREEN
							)
							self.fullscreen = True
				elif event.type == MOUSEBUTTONDOWN:
					if musicBtn.collidepoint(mouse.get_pos()):
						with open("./package/db/database.json", "r") as f:
							data = json.load(f)

						if data["music"] != 0:
							data["music"] = 0
						else:
							data["music"] = 4.2

						with open("./package/db/database.json", "w") as f:
							json.dump(data, f)

						mixer.music.set_volume(data["music"])

						music_btn.make_image()

				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.pause()
					if str(event.key) in ["1073741894"]:
						#print("take screen shot")
						dirc = os.path.expanduser('~')+"\\Pictures\\عملیات رو بردارها\\"
						path = dirc+"{0}.jpg"
						now = datetime.now()
						now = str(now)[:-7].replace(":", "-")
						image.save(self.window, path.format(str(now)))
					if event.key == K_TAB:
						if self.fullscreen:
							self.window = display.set_mode(
								(
									self.window.get_width(),
									self.window.get_height()
								), RESIZABLE
							)
							self.fullscreen = False
						else:
							self.window = display.set_mode(
								(0,0), FULLSCREEN
							)
							self.fullscreen = True

			display.flip()
			display.update()
			clock = time.Clock()
			fps = clock.get_fps()
			clock.tick(fps)

	def game_play(self):
		MachineLevel = LevelsMachine(self.level)

		with open("./package/db/database.json", "r") as f:
			data = json.load(f)

		#mixer.set_num_channels(2)
		mixer.music.load(MachineLevel.level["music_path"])
		mixer.music.set_volume(data["music"])
		mixer.music.play(loops=50)
		#mixer.music.set_pos(float(self.music_pos))

		self.pilBg = MachineLevel.getBackground()

		cards = MachineLevel.makeCards(self.window)

		machine = MachineLevel.makeMachine()

		vallue = machine.newVallue(cards)
		with open("./package/temp2", "r") as f:
			data2 = json.load(f)

		with open("./package/temp", "r") as f:
			data = json.load(f)

		vallue = data["target"]

		if data2["music_pos"] >= 3*60+25:
			data2["music_pos"] = 11

		mixer.music.set_pos(data2["music_pos"])

		timer = MachineLevel.makeTimer()

		VallidCard = 0

		pause_btn = Buttons.pause()

		vallidText = font.FaRender(
			"{0}/{1}".format(str(VallidCard), str(MachineLevel.level["maxVallid"]))
		)

		titleFont = FaFont("./package/fonts/fa.ttf", 70)
		level_name = MachineLevel.level["name"]
		level_name = titleFont.FaRender(
			level_name,
			True, (52, 122, 235)
		)

		mouse.set_cursor(SYSTEM_CURSOR_ARROW)
		selectSleep = 0
		while self.game_play_:
			data2["music_pos"] += mixer.music.get_pos()/100000
			#bg_width = self.bg.get_width()*(
			#	self.window.get_height()+self.window.get_height()/11
			#)/self.bg.get_height()+self.bg.get_height()/3

			#bg = transform.scale(
			#	self.bg,
			#	(
			#		bg_width,
			#		self.window.get_height()
			#	)
			#)
			self.blitBg()

			pause_rect = pause_btn.draw(self.window)
			
			machine.show(self.window)

			self.window.blit(
				level_name,
				(
					pause_rect.x-10-level_name.get_width(),
					pause_rect.y
				)
			)

			color = (4,227,0)

			if timer.getSecond() <= 10:
				color = (247, 77, 4)

			if timer.getSecond() <= 3:
				color = (227, 4, 4)

			text = f"{str(timer.getSecond())} ثانیه وقت دارید!"
			timeText = font.FaRender(text, True, color)

			draw.rect(
				self.window,
				(63, 21, 130),
				(
					self.window.get_width()/2-timeText.get_width()/2, 4,
					timeText.get_width()+6,
					vallidText.get_height()*2+6
				), 0, 13
			)
			self.window.blit(
				timeText,
				(
					self.window.get_width()/2-timeText.get_width()/2,
					2
				)
			)
			
			self.window.blit(
				vallidText,
				(
					self.window.get_width()/2-vallidText.get_width()/2,
					timeText.get_height()+2
				)
			)

			if timer.check():
				self.game_play_ = False
				self.game_over_ = True

			if mouse.get_pressed()[0]:
				if pause_rect.collidepoint(mouse.get_pos()):
					self.pause()

			select = False
			is_selecting = False
			for card in cards:
				card.show(self.window)
				r = card.rect.copy()
				r.w += 20
				r.h += 20
				r.x -= 5
				r.y -= 5
				if card.rect.collidepoint(mouse.get_pos()):
					if mouse.get_pressed()[0]:
						with open("./package/temp", "r") as f:
							vallue = json.load(f)["target"]
						id1 = str(vallue)
						id2 = str(card.id)
						if id2 == id1:
							VallidCard+=1
							#print(VallidCard)
							vallidText = font.FaRender(
								"{0}/{1}".format(
									str(VallidCard), 
									str(MachineLevel.level["maxVallid"])
								)
							)

							fill = (69, 242, 39)
							is_selecting = True
						else:
							if not select:
								fill = (230, 26, 23)
								is_selecting = True
						card.show(self.window, fill)
						
						
						timer = MachineLevel.makeTimer()
						cards = MachineLevel.makeCards(self.window)
						vallue = machine.newVallue(cards)
			if is_selecting:
				display.update()
				time2.sleep(0.03)
		
			#print(str(self.window.get_width())+"x"+str(self.window.get_height()))

			for event in get_ev():
				if event.type == QUIT:sys.exit()
				if event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						self.pause()
					if str(event.key) in ["1073741894"]:
						#print("take screen shot")
						dirc = os.path.expanduser('~')+"\\Pictures\\عملیات رو بردارها\\"
						path = dirc+"{0}.jpg"
						now = datetime.now()
						now = str(now)[:-7].replace(":", "-")
						image.save(self.window, path.format(str(now)))
					if event.key == K_TAB:
						if self.fullscreen:
							self.window = display.set_mode(
								(
									self.window.get_width(),
									self.window.get_height()
								), RESIZABLE
							)
							self.fullscreen = False
						else:
							self.window = display.set_mode(
								(0,0), FULLSCREEN
							)
							self.fullscreen = True
				timer.step(event)
				c = check(event, self.window)
				if c != None:
					self.window = c

			if VallidCard >= MachineLevel.level["maxVallid"]:
				self.game_winn_ = True
				self.game_play_ = False

			clock = time.Clock()
			fps = clock.get_fps()
			clock.tick(fps)
			display.flip()
			display.update()

			with open("./package/temp2", "w") as f:
				json.dump(data2, f)

		#self.music_pos = mixer.music.get_pos()
		mixer.music.set_volume(4.2)

	def game_over(self):
		mixer.music.load("./package/sounds/game_over.mp3")
		mixer.music.play()

		texts = [
			"تا صدای اذان از گلدسته ها بلنده نا امیدی گناه کبیرس"
		]

		text = font.FaRender(
			choice(
				texts
			),
			True,
			(0,0,0)
		)
		#text2 = font.FaRender(
		#	"",
		#	True, (0,0,0)
		#)

		text2 = SlowRender("یه دکمه رو فشار بده و دوباره شروع کن", font, (0,0,0))

		#bg_width = self.bg.get_width()*(
		#	self.window.get_height()+self.window.get_height()/11
		#)/self.bg.get_height()+self.bg.get_height()/3

		#bg = transform.scale(
		#	self.bg,
		#	(
		#		bg_width,
		#		self.window.get_height()
		#	)
		#)

		

		display.update()

		while self.game_over_:
			self.window.fill((0, 0, 0))
			self.blitQatar()

			self.window.blit(
				text,
				(
					self.window.get_width()/2-text.get_width()/2,
					self.window.get_height()/3-text.get_height()/3
				)
			)
			text2.blit(self.window, (
					self.window.get_width()/2-text2.width/2,
					self.window.get_height()/2-text2.height/2+30,
				)
			)

			for event in get_ev():
				if event.type == QUIT:
					sys.exit()
				elif event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
					self.running = False
					self.game_play_ = False
					self.game_over_ = False
					self.game_winn_ = False
					
				if event.type == KEYDOWN:
					if event.key == K_TAB:
						if self.fullscreen:
							self.window = display.set_mode(
								(
									self.window.get_width(),
									self.window.get_height()
								), RESIZABLE
							)
							self.fullscreen = False
						else:
							self.window = display.set_mode(
								(0,0), FULLSCREEN
							)
							self.fullscreen = True
					if event.key == K_ESCAPE:
						self.pause()
					if str(event.key) in ["1073741894"]:
						#print("take screen shot")
						dirc = os.path.expanduser('~')+"\\Pictures\\عملیات رو بردارها\\"
						path = dirc+"{0}.jpg"
						now = datetime.now()
						now = str(now)[:-7].replace(":", "-")
						image.save(self.window, path.format(str(now)))
				c = check(event, self.window)
				if c != None:
					self.window = c

			display.update()

	def game_winn(self):
		with open("./package/db/database.json", "r") as f:
			data = json.load(f)

		if len(data["levels"]) != self.level+1:
			data["levels"][self.level+1]["lock"] = False

		with open("./package/db/database.json", "w") as f:
			json.dump(data, f)

		mixer.music.load("./package/sounds/game_win.mp3")
		mixer.music.play()

		texts = [
			"آفرین",
			"عا لی بود!",
			"تبریک میگم",
			"تو یه نابغه ای!"
		]

		text = font.FaRender(
			choice(texts),
			True,
			(0,0,0)
		)

		text2 = SlowRender("این مرحله رو تموم کردی! ایول", font, (0,0,0))

		self.window.fill((255,4,4))
		#bg_width = self.bg.get_width()*(
		#	self.window.get_height()+self.window.get_height()/11
		#)/self.bg.get_height()+self.bg.get_height()/3

		#bg = transform.scale(
		#	self.bg,
		#	(
		#		bg_width,
		#		self.window.get_height()
		#	)
		#)
		#self.window.blit(
		#	bg, (0,0)
		#)
		

		while self.game_winn_:

			self.window.fill((0,0,0))
			self.blitQatar()
			self.window.blit(
				text,
				(
					self.window.get_width()/2-text.get_width()/2,
					self.window.get_height()/3-text.get_height()/3
				)
			)
			
			text2.blit(self.window, (
					self.window.get_width()/2-text2.width/2,
					self.window.get_height()/2-text2.height/2+30,
				)
			)

			display.update()

			for event in get_ev():
				if event.type == QUIT:sys.exit()
				elif event.type in [MOUSEBUTTONDOWN, KEYDOWN]:
					self.game_winn_ = False
					self.game_over_ = False
					self.game_play_ = False
					self.running = False
					#self.__delete__()
				if event.type == KEYDOWN:
					if event.key == K_TAB:
						if self.fullscreen:
							self.window = display.set_mode(
								(
									self.window.get_width(),
									self.window.get_height()
								), RESIZABLE
							)
							self.fullscreen = False
						else:
							self.window = display.set_mode(
								(0,0), FULLSCREEN
							)
							self.fullscreen = True
					if event.key == K_ESCAPE:
						self.pause()
					if str(event.key) in ["1073741894", str(K_PRINT)]:
						#print("take screen shot")
						dirc = os.path.expanduser('~')+"\\Pictures\\عملیات رو بردارها\\"
						path = dirc+"{0}.jpg"
						now = datetime.now()
						now = str(now)[:-7].replace(":", "-")
						image.save(self.window, path.format(str(now)))

	def run(self):
		while self.running:
			self.starting()
			if self.game_play_:
				self.game_play()
				#self.music_pos = mixer.music.get_pos()
				#with open("./package/temp2", "r") as f:
				#	data = json.load(f)

				#data["music_pos"] = self.music_pos

				#with open("./package/temp2", "w") as f:
				#	json.dump(data, f)
				mixer.music.set_volume(4.2)
			if self.game_over_:
				self.game_over()
			if self.game_winn_:
				self.game_winn()