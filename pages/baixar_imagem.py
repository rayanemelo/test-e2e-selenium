from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaixarImagem:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
    def load(self):
        self.driver.get("https://unsplash.com/pt-br/s/fotografias/new-york?license=free")
        
    def scroll_to_search(self):
      search_result = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='search-photos-route']")))
      self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth' });", search_result)

    def click_first_result(self):
      first_image = self.wait.until(
          EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-masonryposition='1']"))
      )
      first_image.click()
      
    def download_image(self):
      download_link = self.wait.until(
          EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='non-sponsored-photo-download-button']"))
      )
      self.driver.execute_script("arguments[0].click();", download_link)
      