from pygame import *
from ..api import Client
from io import BytesIO
from PIL import Image
from ...FaFont import FaFont, init
init()

class SurfaceGif:
    n = 0
    def __init__(self, fp):
        self.data = Image.open(fp)
        if self.data.format.lower() != "gif":
            raise Exception("this image is not a GIF")
        
    def blit(self, surface:Surface, pos):
        if self.n >= self.data.n_frames:
            self.n = 0

        self.data.seek(self.n)

        data = BytesIO()
        self.data.save(data)
        data = image.load(data)

        surface.blit(data, pos)

        self.n += 1

class Message:
    font = FaFont("./package/fonts/fa.ttf", 30)
    nameFont = FaFont("./package/fonts/fa.ttf", 5)
    def __init__(self, message:dict, client:Client) -> None:
        self.author = message["author"]["username"]+"#"+message["author"]["discriminator"]
        color = (100, 255, 43)
        if message["author"]["id"] != client.user["id"]:
            color = (43, 167, 255)
        self.textSurf = self.font.FaRender(message["content"], True, (255,255,255), color)

    def getSurf(self):
        surf = self.textSurf.copy()
        username = self.nameFont.FaRender(self.author, True, (255,255,255))
        surf.blit(username, (0,0))
        return surf
