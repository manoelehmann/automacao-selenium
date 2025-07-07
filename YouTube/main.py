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
    botao_filtro = navegador.find_elements('id', 'filter-button')
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

time.sleep(0.3)
selecionar_data = navegador.find_elements('id', 'label')
for botao in selecionar_data:
    if 'Data de envio' in botao.text:
        botao.click()
        break

time.sleep(1)
canal = navegador.find_elements('id', 'channel-title')
for botao in canal:
    if 'MaxxSoft Tecnologia' in botao.text:
        botao.click()
        break
time.sleep(0.5)
video = navegador.find_elements('id', 'video-title')
for botao in video:
    if 'WEBINAR - Desvendando o Agronegócio com a MaxxSoft - EP 3' in botao.text:
        botao.click()
        break

'''Devido o uso do AJAX, o teste pode não funcionar em algumas tentativas'''
time.sleep(1000)