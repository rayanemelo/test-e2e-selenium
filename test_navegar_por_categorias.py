import time
from pages.navegar_por_categorias import NavegarPorCategorias

def test_navegar_por_categorias(driver): 
    page = NavegarPorCategorias(driver)
    time.sleep(1)  
    page.navegar_categoria_filmes()
    time.sleep(2) 
    page.navegar_categoria_natureza()
    time.sleep(2) 
    