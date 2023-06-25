from flask import Flask, request
import requests as req, json

app = Flask(__name__)

@app.route("/login")
def login():
    header = {
        "Authorization": f"Bot MTEyMjUyMTgyMTc3NDg4NDk0NQ.GcC9U8.Tvc5F0W2QcX70-kxobS-ICz_4dZRc-UXXLdVD4",
        "Content-Type": "application/json"
    }
    data = json.dumps({})
    url = "https://discord.com/api/v9/guilds/1121421867182465044/members/833370377333243974"
    txt = req.put(url, headers=header, json=data).text
    return txt

app.run(port=7777, debug=True)