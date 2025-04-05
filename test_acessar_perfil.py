import time
from pages.acessar_perfil import AcessarPerfil

def test_buscar(driver): 
    page = AcessarPerfil(driver)
    time.sleep(1)
    page.search_for("blue sky")
    time.sleep(1)
    page.scroll_to_search()
    time.sleep(1)
    page.click_first_result()
    time.sleep(1)
    page.acessar_botao_e_perfil() 
    