from __future__ import annotations

from pages.basepage import BasePage
from pages.newspage.news_page_locators_collection import NewsPageLocatorCollection


class NewsPage(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)
        self.__locators = NewsPageLocatorCollection()

    def __search_field_write_text(self) -> None:
        self._click_on_element(self.__locators.filter_button)
        element = self._driver.find_element_by_xpath(self.__locators.search_field)
        element.send_keys("Dakar")

    def get_search_result(self) -> str:
        self.__search_field_write_text()
        self._wait_text(self.__locators.search_field_result_first, "Dakar")
        return self._driver.find_element_by_xpath(self.__locators.search_field_result).text
