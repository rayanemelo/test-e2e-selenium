from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavegarPorCategorias:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navegar_categoria_filmes(self):
        categoria_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/pt-br/t/film']"))
        )
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/pt-br/t/film']"))
        )
        categoria_element.click()

    def navegar_categoria_natureza(self):
        categoria_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/pt-br/t/nature']"))
        )
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/pt-br/t/nature']"))
        )
        categoria_element.click()
