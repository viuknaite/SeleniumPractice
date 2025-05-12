import pytest
from pages.main_page import MainPage
from pages.english_ver import EnglishVersion
from pages.qa_ver import QaVersion
from pages.mario_ver import MarioVersion
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
        main_page = MainPage(self.browser)
        main_page.open()
        assert "Wikipedia" in self.browser.title
        main_page.click_english_link()

        self.browser.implicitly_wait(10)

        eng_page = EnglishVersion(self.browser)
        eng_page.click_search_icon()
        eng_page.enter_search_text("qa engineer")
        eng_page.click_search_button()

        self.browser.implicitly_wait(10)

        qa_page = QaVersion(self.browser)
        qa_page.open_first_result_in_new_tab()
        assert qa_page.page_contains_text("Wikipedia")

        self.browser.implicitly_wait(10)

        mario_page = MarioVersion(self.browser)
        mario_page.click_s_i()
        mario_page.enter_s_t("mario")
        mario_page.click_s_b()

        #TODO create 2 files with 1 class each
