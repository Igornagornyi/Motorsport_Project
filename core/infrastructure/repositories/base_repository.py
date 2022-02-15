from sqlalchemy import create_engine

from sqlalchemy.orm import Session, sessionmaker

from core.configs.config import Config

from core.singleton import Singleton


class BaseRepository(Singleton):
    def __init__(self) -> None:
        self.__config = Config()

        self.__engine = create_engine(f"{self.__config.database.driver_name}://{self.__config.database.user}:"
                                      f"{self.__config.database.password}@{self.__config.database.host}:"
                                      f"{self.__config.database.port}/{self.__config.database.database}")
        self.session: Session = sessionmaker(self.__engine)()
