from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class QaVersion:
    def __init__(self, browser):
        self.browser = browser

    def open_first_result_in_new_tab(self):
        # Явное ожидание загрузки результатов
        first_link = WebDriverWait(self.browser, 1000).until(
            EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'mw-body-content')]//a)[1]"))
        )
        href = first_link.get_attribute("href")
        self.browser.execute_script(f"window.open('{href}', '_blank');")
        self.browser.switch_to.window(self.browser.window_handles[1])
        print(self.browser.window_handles)
        # self.browser.switch_to.window(self.browser.window_handles[0])
        cookies = self.browser.get_cookies()
        print(cookies)
        self.browser.add_cookie({
            "name": "test_cookie",
            "value": "12345",
            "domain": "wikipedia.org"
        })
        cookies = self.browser.get_cookies()
        print(cookies)

    def page_contains_text(self, text):
        # Проверка заголовка страницы
        if text.lower() in self.browser.title.lower():
            return True

        # Проверка содержимого страницы
        body_text = self.browser.find_element(By.TAG_NAME, "body").text
        return text.lower() in body_text.lower()