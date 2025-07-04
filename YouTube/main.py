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

navegador.find_element('class name', 'yt-spec-button-shape-next.yt-spec-button-shape-next--text.yt-spec-button-shape-next--mono').click()


'''FAZER UMA AUTOMAÇÃO PARA PESQUISAR O VIDEO MAIS RECENTE DA MAXXSOFT USANDO FILTRO'''



time.sleep(1000)