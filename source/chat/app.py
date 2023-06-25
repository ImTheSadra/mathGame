from pygame import *
from .api import is_anonymous, login, Client
from .graphics import Login
from ..FaFont import FaFont, SlowRender
import sys
from threading import Thread

class App:
    font = FaFont("./package/fonts/fa.ttf", 24)
    client = None
    def __init__(self, window:Surface) -> None:
        mouse.set_cursor(SYSTEM_CURSOR_WAIT)
        self.window = window
        def setClient():
            try:self.client = Client()
            except:
                #self.client = 0
                #print(err.args[0])
                data = Login(window)
                data = data.giveFormData()
                login(data["login"], data["password"])
                self.client = Client()
        #Thread(target=setClient).start()
        setClient()
        txt = SlowRender("درحال بارگذاری...", FaFont("./package/fonts/fa.ttf", 100), (0,0,0))
        while self.client == None:
            self.window.fill((255,255,255))

            txt.blit(
                self.window,
                (
                    self.window.get_width()/2-txt.width/2,
                    self.window.get_height()/2-txt.height/2
                )
            )
            
            for ev in event.get():
                if ev.type == QUIT:sys.exit()

            display.update()
            
    title = SlowRender("از دبیر مشاوره بگیر", font, (255,255,255))
    def blitMessages(self):
        if self.client.messages == []:
            draw.rect(
                self.window,
                (99, 155, 207),
                (
                    0, 0, self.window.get_width(),
                    80
                ), 0, border_bottom_left_radius=5,
                border_bottom_right_radius=5
            )
            return
        
        countOfMess = len(self.client.messages)
        oy = self.window.get_height()-200

        for message in self.client.messages:
            surf:Surface = message["surf"]
            
            x = 5
            if message["fm"]:
                x = self.window.get_width()-surf.get_width()-5

            self.window.blit(
                surf,
                (
                    x, oy
                )
            )

            oy -= surf.get_height()

        
        draw.rect(
            self.window,
            (99, 155, 207),
            (
                0, 0, self.window.get_width(),
                80
            ), 0, border_bottom_left_radius=5,
            border_bottom_right_radius=5
        )
        self.title.blit(self.window, 
            (
                self.window.get_width()/2-self.title.width/2,
                80/2-self.title.height/2
            ), 0.1
        )
            

    def chatting(self):
        demoMessage = ""
        bg = image.load("./package/images/backgrounds/chat.jpg")
        mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        while True:
            self.window.fill((0,0,0))
            self.window.blit(
                transform.scale(
                    bg, 
                    (
                        self.window.get_width(),
                        self.window.get_height()
                    )
                ), (0,0)
            )
            self.blitMessages()

            displayTxt = demoMessage
            if demoMessage == "":
                displayTxt = " یه پیام بنویس بعد دکمه اینتر رو فشار بده :) "
            text = self.font.FaRender(displayTxt, True, (255,255,255), (164, 165, 166))
            self.window.blit(
                text,
                (
                    self.window.get_width()-5-text.get_width(),
                    self.window.get_height()-5-text.get_height()
                )
            )

            for ev in event.get():
                if ev.type == QUIT:
                    self.client.running=False
                    sys.exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_BACKSPACE:
                        demoMessage = demoMessage[:-1]
                        #continue
                    elif ev.unicode == '\x1b':
                        self.client.running = False
                        return
                    elif ev.unicode == "\r":
                        Thread(target=self.client.sendMessage, args=[demoMessage]).start()
                    
                        color = (103, 214, 75)
                        #self.client.messages.append(
                        #    {
                        #        "content": demoMessage,
                        #        "author": self.client.author,
                        #        "surf": self.font.FaRender(demoMessage, True, (255,255,255), color),
                        #        "fm": True
                        #    }
                        #)
                        demoMessage = ""
                        #continue
                    else:demoMessage += ev.unicode

            clock = time.Clock()
            clock.tick(clock.get_fps())
            display.update()