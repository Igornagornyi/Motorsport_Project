from singleton import Singleton


class LocalStorage(Singleton):
    def __init__(self):
        self.__is_actual = False
        self.data = "window.localStorage['am-uid'] = 'f9eb889c52c84f1cbbbec1abb0ffb32c';"

    def storage_data(self) -> str:
        if self.__is_actual:
            return self.data
        else:
            self.data = self.data
            self.__is_actual = True
            return self.data
