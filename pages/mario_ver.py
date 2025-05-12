from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MarioVersion:
    def __init__(self, browser):
        self.browser = browser

    def click_s_i(self):
        self.browser.find_element(By.XPATH, "//div[@id='p-search']//a").click()

    def enter_s_t(self, text):
        search_input = WebDriverWait(self.browser, 1000).until(
            EC.presence_of_element_located((By.XPATH, "(//input[@class='cdx-text-input__input'])[1]"))
        )
        search_input.send_keys(text)
        self.browser.implicitly_wait(50)

    def click_s_b(self):
        button = WebDriverWait(self.browser, 1000).until(
            EC.presence_of_element_located((By.XPATH, "//div//form[@id='searchform']//button"))
        )
        button.click()

