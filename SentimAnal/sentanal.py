import requests
import json
import aiohttp
import asyncio

def SentAnal(text):
    _url = "https://sentim-api.herokuapp.com/api/v1/"
    _header = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    _data = {"text": text}


    data = requests.post(_url, headers=_header, json=_data).text
    print(data)
    data = json.loads(data)
    res = data["result"]
    pol = res["polarity"]
    typ = res["type"]
    return pol


if __name__ == "__main__":
    s = SentAnal('HEllo')
    print(s)
