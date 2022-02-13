import pytest

from core.cookie import Cookie

from selenium.webdriver import Chrome

from core.configs.config import Config

from core.local_storage import LocalStorage

from pages.newspage.newspage import NewsPage

from pages.homepage.homepage import HomePage

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
def config() -> Config:
    yield Config()


@pytest.fixture(scope="session")
def cookie() -> Cookie:
    yield Cookie()


@pytest.fixture(scope="session")
def localstorage() -> LocalStorage:
    yield LocalStorage()


@pytest.fixture(scope="session")
def driver(config, cookie, localstorage) -> Chrome:
    driver = Chrome(ChromeDriverManager().install())
    driver.get(config.host)
    driver.add_cookie(cookie.cookie_data())
    driver.execute_script(localstorage.storage_data())
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def homepage(driver):
    yield HomePage(driver)


@pytest.fixture(scope="session")
def newspage(driver):
    yield NewsPage(driver)
