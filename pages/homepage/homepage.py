from pages.basepage import BasePage
from pages.newspage.newspage import NewsPage
from pages.homepage.homepage_locators_collection import HomePageLocatorCollection


class HomePage(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)
        self.__locators = HomePageLocatorCollection()

    def check_subscribe_item_title(self) -> str:
        self._scroll_to_the_element(self.__locators.subscribe_button)
        return self._driver.find_element_by_xpath(self.__locators.subscribe_button).text

    def click_onetrust(self):
        self._click_on_element(self.__locators.onetrust_button)

    def select_news(self) -> NewsPage:
        self._click_on_element(self.__locators.news_button)
        return NewsPage(self._driver)
