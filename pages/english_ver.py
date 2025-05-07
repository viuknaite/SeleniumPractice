import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException


class EnglishVersion:
    def __init__(self, browser):
        self.browser = browser

    def save_screenshot(self, step_name):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"screenshots/{step_name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.browser.save_screenshot(filename)
        print(f"[!] Скриншот сохранён: {filename}")

    def click_search_icon(self):
        try:
            self.browser.find_element(By.XPATH, "//div[@id='p-search']//a").click()
            self.save_screenshot("click_search_icon")
        except Exception as e:
            self.save_screenshot("error_click_search_icon")
            raise e

    def enter_search_text(self, text):
        try:
            search_input = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[@class='cdx-text-input__input'])[1]"))
            )
            search_input.send_keys(text)
            self.browser.implicitly_wait(3)
            self.save_screenshot("enter_search_text")
        except Exception as e:
            self.save_screenshot("error_enter_search_text")
            raise e

    def click_search_button(self):
        wait = WebDriverWait(self.browser, 10)
        for i in range(3):
            try:
                button = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "button.cdx-search-input__end-button"))
                )
                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cdx-search-input__end-button"))
                ).click()
                self.save_screenshot("click_search_button")
                return
            except (StaleElementReferenceException, TimeoutException):
                time.sleep(1)
        self.save_screenshot("error_click_search_button")
        raise Exception("Не удалось кликнуть по кнопке поиска")

    def handle_cookies(self):
        try:
            cookies = self.browser.get_cookies()
            print("До добавления куки:", cookies)

            self.browser.add_cookie({
                "name": "test_cookie",
                "value": "12345",
                "domain": "wikipedia.org"
            })

            cookies = self.browser.get_cookies()
            print("После добавления куки:", cookies)
            self.save_screenshot("handle_cookies")
        except WebDriverException as e:
            self.save_screenshot("error_handle_cookies")
            raise e

    def open_first_result_in_new_tab(self):
        for i in range(3):
            try:
                first_link = WebDriverWait(self.browser, 10).until(
                    EC.presence_of_element_located((By.XPATH, "(//div[contains(@class, 'mw-body-content')]//a)[1]"))
                )
                href = first_link.get_attribute("href")
                self.browser.execute_script(f"window.open('{href}', '_blank');")
                self.browser.switch_to.window(self.browser.window_handles[1])
                self.handle_cookies()
                self.save_screenshot("open_first_result_in_new_tab")
                return
            except StaleElementReferenceException:
                time.sleep(1)
        self.save_screenshot("error_open_first_result")
        raise Exception("Не удалось открыть первую ссылку")
