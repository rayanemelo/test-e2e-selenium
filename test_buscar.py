import time
from pages.buscar import Buscar

def test_buscar(driver): 
    page = Buscar(driver)
    time.sleep(1)  
    page.search_for("orange cat")
    time.sleep(1) 
    page.scroll_to_search()
    time.sleep(1) 
    page.click_first_result()