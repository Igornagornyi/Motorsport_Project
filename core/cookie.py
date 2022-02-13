from core.singleton import Singleton


class Cookie(Singleton):
    def __init__(self):
        self.__is_actual = False
        self.data = {'name': '_gcl_au', 'value': '1.1.1004345675.1644399482'}

    def cookie_data(self) -> dict:
        if self.__is_actual:
            return self.data
        else:
            self.data = self.data
            self.__is_actual = True
            return self.data
