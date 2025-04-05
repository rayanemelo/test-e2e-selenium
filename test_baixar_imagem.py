import time
from pages.baixar_imagem import BaixarImagem

def test_baixar_imagem(driver): 
    page = BaixarImagem(driver)
    time.sleep(1)
    page.load()
    time.sleep(1)
    page.scroll_to_search()
    time.sleep(1)
    page.click_first_result()
    time.sleep(1)
    page.download_image()
    