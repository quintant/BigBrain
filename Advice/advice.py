
import requests
import json

class Advice:
    def __init__(self) -> None:
        self._url = "https://api.adviceslip.com/advice"

    def random(self) -> str:
        data = requests.get(self._url).text
        data = json.loads(data)
        if 'slip' in data:
            return data['slip']['advice']
        else:
            return 'Something went wrong. :('



if __name__ == "__main__":
    a = Advice()
    print(a.random())