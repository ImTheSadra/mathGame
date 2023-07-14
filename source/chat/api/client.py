from requests import Session
import json, aiohttp, asyncio, sys, time
from io import BytesIO
from PIL import Image
from pygame import image
from threading import Thread
from ...FaFont import FaFont

def is_anonymous():
    with open("./package/db/database.json", "r") as f:
        data = json.load(f)
    return data["discord"] == None

class Client:
    running = True
    messages = []
    font = FaFont("./package/fonts/fa.ttf", 24)
    
    def __init__(self):
        
        with open("./package/db/database.json", "r") as f:
            data = json.load(f)
        if data["discord"]["token"] == None:
            raise Exception("login anjam nashod!")
        self.headers = {
            "authorization": data["discord"]["token"]
        }
        
        payload = {
            "op": 2,
            "d": {
                "token": data["discord"]["token"],
                "intents": 513,
                "properties": {
                    "$os": "linux",
                    "$browser": "zeroSpeedDown",
                    "$device": "zeroPc"
                }
            }
        }

        self.channelId = "1121811139995644015"
        self.session = Session()
        self.session.headers = self.headers
        self.author = self.getUser("@me")

        self.session.post("https://discord.com/api/v9/invites/cV6zH7gkvn", headers=self.headers)

        async def on_message(ws, message:aiohttp.WSMessage):
            data = json.loads(message.data)
            if data["t"] != "MESSAGE_CREATE":
                return
            json.dump(data, open("./test.json", "w"))
            if data['d']['channel_id'] != self.channelId:
                return
            if data['d']["content"] == "":
                return
            if data["d"]["author"]["id"] != self.author["id"]:
                return
            
            color = (75, 91, 214)
            self.messages.append(
                {
                    "content": data['d']["content"],
                    "author": data['d']["author"],
                    "surf": self.font.FaRender(data['d']["content"], True, (255,255,255), color),
                    "fm": False
                }
            )
        
        async def main():
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect("wss://gateway.discord.gg/?v=9&encoding=json") as ws:
                    await ws.send_json(payload)
                    async for message in ws:
                        if not self.running:
                            return
                        await on_message(ws, message)
        
        loop = asyncio.get_event_loop()
        
        def handelMessages():
            if not self.running:
                return
            messages = self.getMessages()
            messagesE = []
            for message in messages:
                color = (75, 91, 214)
                fm = False
                if message["author"]["id"] == self.author["id"]:
                    color = (103, 214, 75)
                    fm = True
                surf = self.font.FaRender(message["content"], True, (255,255,255), color)
                msg = {
                    "author": message["author"],
                    "content": message["content"],
                    "surf": surf,
                    "fm": fm
                }
                messagesE.append(msg)
            self.messages = messagesE
            time.sleep(0.5)
            handelMessages()
        Thread(target=handelMessages).start()
        #Thread(target=loop.run_until_complete, args=[main()]).start()

    def getMessages(self, limit=20):
        url = "https://discord.com/api/v9/channels/"+self.channelId+"/messages?limit="+str(limit)
        data = self.session.get(url).json()
        return data


    def sendMessage(self, content:str):
        url = "https://discord.com/api/v9/channels/"+self.channelId+"/messages"

        data = {
            "content": content
        }
        
        data = self.session.post(
            url, data=data, headers=self.headers
        )
        
        return data.json()

    def getUser(self, userId:str):
        url = "https://discord.com/api/v9/users/"+userId
        data = self.session.get(url).json()
        return data
    
    def getUserAvatar(self, userId:str):
        user = self.getUser(userId)
        avatarUrl = "https://cdn.discord.com/avatars/"+user["avatar"]
        content = self.session.get(avatarUrl+".gif")
        if content.status_code != 200:
            content = self.session.get(avatarUrl+".png")

        data = BytesIO().write(content.content)
        return (image.load(data), Image.open(data))
