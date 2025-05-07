from selenium.webdriver.common.by import By

class ArticlePage:
    def __init__(self, browser):
        self.browser = browser

    def page_contains_text(self, text):
        if text.lower() in self.browser.title.lower():
            return True
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        return text.lower() in body_text.lower()
