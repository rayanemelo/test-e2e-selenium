from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Anunciar:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_anunciar(self):
        anunciar_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/pt-br/anunciar']"))
        )
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/pt-br/anunciar']"))
        )
        anunciar_button.click()
    
    def click_anunciar_button(self):
        anunciar_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='https://unsplash.typeform.com/advertise']"))
        )
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='https://unsplash.typeform.com/advertise']"))
        )
        anunciar_button.click()
        
    def inserir_input_value(self, nome): 
      input = self.wait.until(
          EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type your answer here...']"))
      )
      
      input.send_keys(nome + Keys.ENTER)
      
    def inserir_email(self, email): 
      input = self.wait.until(
          EC.presence_of_element_located((By.XPATH, "//input[@type='email']"))
      )
      input.send_keys(email + Keys.ENTER)
    
    def selecionar_opcao(self):
      opcao = self.wait.until(
          EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Performance']"))
      )
      opcao.click()
    
    def submit(self):
      submit_button = self.wait.until(
          EC.presence_of_element_located((By.XPATH, "//button[@data-qa='submit-button deep-purple-submit-button']"))
      )
      submit_button.click()

     
