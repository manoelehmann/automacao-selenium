from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome()
navegador.get('https://www.youtube.com/')
navegador.maximize_window()

navegador.find_element('class name', 'ytSearchboxComponentInput.yt-searchbox-input.title').send_keys('Maxxsoft')
navegador.find_element('class name', 'ytSearchboxComponentSearchButton').click()





'''FAZER UMA AUTOMAÇÃO PARA PESQUISAR O VIDEO MAIS RECENTE DA MAXXSOFT USANDO FILTRO'''



time.sleep(1000)