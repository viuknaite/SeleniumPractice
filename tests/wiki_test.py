import pytest
import allure
from selenium import webdriver
from pages.main_page import MainPage
from pages.english_ver import EnglishVersion
from pages.article_page import ArticlePage


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome()
    request.cls.browser = driver
    yield
    driver.quit()


@pytest.mark.usefixtures("browser")
class TestSearch:

    @allure.title("Проверка поиска статьи по запросу 'qa engineer'")
    @allure.severity(allure.severity_level.CRITICAL)
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
        eng_page.open_first_result_in_new_tab()

        article_page = ArticlePage(self.browser)
        assert article_page.page_contains_text("Wikipedia")