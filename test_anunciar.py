import time
from pages.anunciar import Anunciar

def test_anunciar(driver): 
    page = Anunciar(driver)
    time.sleep(1)
    page.click_anunciar()
    time.sleep(1)
    page.click_anunciar_button()
    time.sleep(1)
    page.inserir_input_value("Teste Selenium")
    time.sleep(1)
    page.inserir_email("teste@selenium.com")
    time.sleep(1)
    page.inserir_input_value("Pytest Selenium Company")
    time.sleep(1)
    page.selecionar_opcao()
    time.sleep(1)
    page.submit()