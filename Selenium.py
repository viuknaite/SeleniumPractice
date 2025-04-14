from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.wikipedia.org/")



# Implicit wait
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//a//*[contains(text(), 'English')]").click()
driver.find_element(By.XPATH, '//input').send_keys("qa engineer")

# Expicit wait for an element to appear
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(By.XPATH, "//button[contains(text(), 'Search')]").click()
)

driver.implicitly_wait(10)

driver.quit()