from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.url = "https://www.wikipedia.org/"

    def open(self):
        self.browser.get(self.url)

    def click_english_link(self):
        self.browser.find_element(By.XPATH, "//a//*[contains(text(), 'English')]").click()
