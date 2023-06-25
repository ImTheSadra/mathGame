from requests import Session
import json

def joinGuild(token:str, uID:str):
    url = "https://discord.com/api/v9/guilds/1121421867182465044/members/"+uID
    res = Session().post(url, {"Authorization": token})
    print(res.text)

def login(login:str, password:str):
    req = Session()
    url = "https://discord.com/api/v9/auth/login"
    loginData = {
        "login": login,
        "password": password
    }
    headers = {'Content-Type': 'application/json'}
    result = req.post(url, json=loginData, headers=headers).json()

    with open("./package/db/database.json", "r") as f:
        data = json.load(f)
    
    data["discord"] = result

    with open("./package/db/database.json", "w") as f:
        json.dump(data, f)