import os


class ServerInfo:

    def __init__(self):
        self.host = os.environ.get('HOST')
        self.port = os.environ.get('PORT')
        self.username = os.environ.get('USERNAME')
        self.pw = os.environ.get('PASSWORD')
