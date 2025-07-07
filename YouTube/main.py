from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome()
navegador.get('https://www.youtube.com/')
navegador.maximize_window()
espera = WebDriverWait(navegador, 20)

navegador.find_element('class name', 'ytSearchboxComponentInput.yt-searchbox-input.title').send_keys('Maxxsoft')
clicar_pesquisar = navegador.find_element('class name', 'ytSearchboxComponentSearchButton')
clicar_pesquisar.click()
time.sleep(1)

def filtro(navegador):
    botao_filtro = navegador.find_elements('class name', 'style-scope.ytd-search-header-renderer')
    for botao in botao_filtro:
        if 'Filtros' in botao.text:
            botao.click()
            break
filtro(navegador)

selecionar_filtro = navegador.find_elements('id', 'label')
for botao in selecionar_filtro:
    if 'Canal' in botao.text:
        botao.click()
        break
time.sleep(1)

filtro(navegador)
selecionar_data = navegador.find_elements('id', 'endpoint')
for botao in selecionar_data:
    if 'Data de envio' in botao.text:
        botao.click()
        break

time.sleep(1000)