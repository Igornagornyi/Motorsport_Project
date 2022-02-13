from ..configs.test_rail_config import TestRailConfig
from singleton import Singleton


class Config(Singleton):
    def __init__(self):
        self.host = "https://www.motorsport.com/"
        self.driver_path = "core/infrastructure/bin/chromedriver"
        self.test_rail = TestRailConfig()
