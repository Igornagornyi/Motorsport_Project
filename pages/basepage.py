from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from core.page_object_singleton import PageObjectSingleton


class BasePage(PageObjectSingleton):
    def __init__(self, driver: Chrome = None) -> None:
        super().__init__(driver)
        self.wait = WebDriverWait(self._driver, 20)

    def _click_on_element(self, by: str) -> None:
        element = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, by)
            )
        )
        element.click()

    def _wait_text(self, by: str, text: str) -> None:
        element = self.wait.until(
            EC.text_to_be_present_in_element(
                (By.XPATH, by), text
            )
        )
        return element

    def _scroll_to_the_element(self, by: str) -> None:
        target = self._driver.find_element_by_xpath(by)
        actions = ActionChains(self._driver)
        actions.move_to_element(target).perform()

    def _go_to_url(self, url: str):
        self._driver.get(url)
