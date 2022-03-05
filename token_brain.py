

class Token(str):
    def __new__(cls, *args, **kwargs):
        with open('giga-brain.re') as f:
            pre_token = f.readline()
            token = pre_token.strip()
        return str.__new__(cls, token, *args, **kwargs)