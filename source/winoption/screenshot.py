from pygame import Surface, image
from datetime import datetime

def takeScreenShot(win:Surface):
	path = "Libraries/Pictures/{0}.jpg"
	now = datetime.now().date()
	image.save(win, path.format(now))