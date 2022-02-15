import pytest

from core.result import Result

from core.infrastructure.repositories.test_result_repository import TestResultRepository

from core.cookie import Cookie

from selenium.webdriver import Chrome

from core.configs.config import Config

from core.local_storage import LocalStorage

from pages.newspage.newspage import NewsPage

from pages.homepage.homepage import HomePage

from webdriver_manager.chrome import ChromeDriverManager


results = []


@pytest.fixture(scope="session")
def config() -> Config:
    yield Config()


@pytest.fixture(scope="session")
def test_result_repository() -> TestResultRepository:
    yield TestResultRepository()


@pytest.fixture(scope="session")
def cookie() -> Cookie:
    yield Cookie()


@pytest.fixture(scope="session")
def localstorage() -> LocalStorage:
    yield LocalStorage()


@pytest.fixture(scope="session")
def driver(config, cookie, localstorage, test_result_repository) -> Chrome:
    driver = Chrome(ChromeDriverManager().install())
    driver.get(config.host)
    driver.add_cookie(cookie.cookie_data())
    driver.execute_script(localstorage.storage_data())
    driver.maximize_window()
    yield driver
    test_result_repository.save_all(Result.from_test_reports(
        results, "UI"
        )
    )
    driver.quit()


@pytest.fixture(scope="session")
def homepage(driver):
    yield HomePage(driver)


@pytest.fixture(scope="session")
def newspage(driver):
    yield NewsPage(driver)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call":
        results.append(result)
