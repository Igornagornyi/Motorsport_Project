from core.configs.db_config import DBconfig
from core.configs import TestRailConfig

from core.singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.host = "https://www.motorsport.com/"
        self.test_rail = TestRailConfig()
        self.data_base = DBconfig()
