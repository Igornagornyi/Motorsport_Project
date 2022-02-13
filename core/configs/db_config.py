from core.singleton import Singleton


class DBconfig(Singleton):
    def __init__(self):
        self.driver_name = "postgresql+psycopg2"
        self.database = "store"
        self.host = "localhost"
        self.port = "5432"
        self.user = "postgres"
        self.password = "ihorpostgres"
