from ..tts import TTS

tts = TTS()

class Game:
	def __init__(self, level:int):
		self.level = level

	async def run()