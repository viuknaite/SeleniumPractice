import os
import time
from selenium.webdriver.common.by import By


class ArticlePage:
    def __init__(self, browser):
        self.browser = browser

    def save_screenshot(self, name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        path = f"screenshots/{name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.browser.save_screenshot(path)
        print(f"[!] Скриншот сохранён: {path}")

    def page_contains_text(self, text):
        try:
            if text.lower() in self.browser.title.lower():
                self.save_screenshot("check_title_success")
                return True
            body_text = self.browser.find_element(By.TAG_NAME, "body").text
            if text.lower() in body_text.lower():
                self.save_screenshot("check_body_success")
                return True
            self.save_screenshot("text_not_found")
            return False
        except Exception as e:
            self.save_screenshot("error_check_text")
            raise e
