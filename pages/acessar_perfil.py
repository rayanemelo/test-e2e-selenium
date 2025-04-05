from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AcessarPerfil:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_for(self, term):
        search_input = self.wait.until(
            EC.presence_of_element_located((By.NAME, "searchKeyword"))
        )
        search_input.clear()
        search_input.send_keys(term)
        search_input.submit()

    def scroll_to_search(self):
        search_result = self.wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[data-testid='search-photos-route']")
            )
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({ behavior: 'smooth' });", search_result
        )

    def click_first_result(self):
        first_image = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-masonryposition='1']"))
        )
        first_image.click()

    def acessar_perfil(self):
        perfil = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".Pgpa9"))
        )
        perfil.click()

    def acessar_botao_e_perfil(self):
        containers = self.driver.find_elements(By.CSS_SELECTOR, ".XrA3r")

        if containers:
            try:
                botao = containers[0].find_element(
                    By.CSS_SELECTOR, "button[type='button']"
                )
                self.wait.until(EC.element_to_be_clickable(botao))
                botao.click()
                print("Botão clicado com sucesso.")
                self.acessar_perfil()  
            except:
                print("Botão não encontrado ou não clicável.")
        else:
            print("Elemento .XrA3r não encontrado.")
