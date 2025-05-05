import pytest
from pages.main_page import MainPage
from selenium import webdriver

@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    request.cls.browser = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("browser")
class TestSearch:
    def test_search_qa_engineer(self):
        page = MainPage(self.browser)
        page.open()
        assert "Wikipedia" in self.browser.title

        self.browser.implicitly_wait(10)
        page.click_english_link()
        page.click_search_icon()
        page.enter_search_text("qa engineer")
        page.click_search_button()
        page.open_first_result_in_new_tab()

        assert page.page_contains_text("Wikipedia")
