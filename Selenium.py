from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    request.cls.browser = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("browser")
class TestBrowserExample:
    def test_example(self):
        self.browser.get("https://www.wikipedia.org/")
        assert "Wikipedia" in self.browser.title

        # Implicit wait
        self.browser.implicitly_wait(10)
        self.browser.find_element(By.XPATH, "//a//*[contains(text(), 'English')]").click()
        self.browser.find_element(By.XPATH, "//div[@id='p-search']//a").click()
        self.browser.find_element(By.XPATH, "//input[@class='cdx-text-input__input']").send_keys("qa engineer")

        # Explicit wait for an element to appear
        element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div//form[@id='searchform']//button"))
        )
        element.click()

        self.browser.quit()
