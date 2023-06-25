from pygame import *
from ...FaFont import FaFont, SlowRender
import sys

class Login:
    font = FaFont("./package/fonts/fa.ttf", 30)
    def __init__(self, window:Surface) -> None:
        mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        self.window = window

    def giveFormData(self):
        loginData = {
            "login": "",
            "password": ""
        }
        select = "login"
        bg = image.load("./package/images/backgrounds/chat.jpg")

        btnText = self.font.FaRender("ورود", True, (255,255,255))

        txt = SlowRender("وارد اکانت خود شوید", self.font, (255,255,255), (0,0,0))
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
            txt.blit(
                self.window,
                (
                    self.window.get_width()/2-txt.width/2,
                    self.window.get_height()/5-txt.height/2
                ), 0.1
            )

            button = draw.rect(
                self.window,
                (52, 97, 186),
                (
                    self.window.get_width()/2-btnText.get_width()/2,
                    self.window.get_height()/5*4-btnText.get_height()/2,
                    btnText.get_width(),
                    btnText.get_height()
                ), 0, 5
            )

            self.window.blit(
                btnText,(button.x, button.y)
            )

            w = 200
            h = 32
            text = None
            if loginData["login"] != "":
                text = self.font.FaRender(loginData["login"], True, (0,0,0))
                w = text.get_width()
                h = text.get_height()
            loginInput = Rect(
                self.window.get_width()/2-w/2,
                self.window.get_height()/3-h/2,
                w+6, h+6
            )

            color = (255,255,255)
            if select == "login":
                color = (210,210,210)
            draw.rect(
                self.window,
                color,
                loginInput,
                0, 5
            )

            if text != None:
                self.window.blit(
                    text,(
                        loginInput.x+3,
                        loginInput.y+3
                    )
                )

            w = 200
            h = 32
            text = None
            if loginData["password"] != "":
                text = self.font.FaRender(loginData["password"], True, (0,0,0))
                w = text.get_width()
                h = text.get_height()
            passwordInput = Rect(
                self.window.get_width()/2-w/2,
                self.window.get_height()/3*2-h/2,
                w+6, h+6
            )

            color = (255,255,255)
            if select == "password":
                color = (210,210,210)

            draw.rect(
                self.window,
                color,
                passwordInput,0,
                5
            )

            if text != None:
                self.window.blit(
                    text,(
                        passwordInput.x+3,
                        passwordInput.y+3
                    )
                )

            for ev in event.get():
                if ev.type == QUIT:sys.exit()
                if ev.type == KEYDOWN:
                    if ev.key == K_BACKSPACE:
                        loginData[select] = loginData[select][:-1]
                    elif ev.key == K_ESCAPE:
                        return
                    elif ev.key == K_RETURN:
                        if loginData["login"] == "" or loginData["password"] == "":
                            continue
                        return loginData
                    else:
                        loginData[select] += ev.unicode
                elif ev.type == MOUSEBUTTONDOWN:
                    if passwordInput.collidepoint(ev.pos):
                        select = "password"
                    elif loginInput.collidepoint(ev.pos):
                        select = "login"
                    elif button.collidepoint(ev.pos):
                        mouse.set_cursor(SYSTEM_CURSOR_WAIT)
                        return loginData
            
            clock = time.Clock()
            clock.tick(clock.get_fps())
            display.update()