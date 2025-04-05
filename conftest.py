import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture
# def driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless") 
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.get("https://unsplash.com/pt-br/")
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080") 
    options.binary_location = "/usr/bin/chromium"

    driver = webdriver.Chrome(options=options)
    driver.get("https://unsplash.com/pt-br/")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()