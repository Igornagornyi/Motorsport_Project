from singleton import Singleton


class TestRailConfig(Singleton):
    def __init__(self):
        self.host = "https://testrail.com"
        self.access_token = "sd123"
