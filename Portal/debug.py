from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

navegador = webdriver.Chrome()
navegador.get('https://sei.esup.edu.br/index.xhtml')
navegador.maximize_window()

espera = WebDriverWait(navegador, 15)

                         # estrutura de login

navegador.find_element('id', 'form:usuario').send_keys('71550403125')
navegador.find_element('id', 'form:senha').send_keys('@Neto07342')
navegador.find_element('id', 'form:loginBtn:loginBtn').click()
time.sleep(5)

                         # percorrer lista, achar e clicar no financeiro

financeiro = navegador.find_elements('class name', 'nav-item.collapsed.dcjq-current-parent.dcjq-parent-li')
for botao in financeiro:
    if 'Financeiro' in botao.text:
        espera.until(EC.element_to_be_clickable(botao))
        botao.click()
        break

                          # clicar na opção pequena do financeiro

mini_financeiro = navegador.find_element('id', 'clink16')
espera.until(EC.element_to_be_clickable(mini_financeiro))
mini_financeiro.click()

                          # função para selecionar opções

def selecionar_opcao(navegador, texto_opcao):
    percorrer_lista = navegador.find_element('id', 'form:selectItemSituacaoContaReceberConsultar')
    selecionar = Select(percorrer_lista)
    selecionar.select_by_visible_text(texto_opcao)

    clicar = navegador.find_element('id', 'form:mmConsultarContasAPagar:mmConsultarContasAPagar')
    espera.until(EC.element_to_be_clickable(clicar)).click()
    time.sleep(1.5)

selecionar_opcao(navegador, 'Em Aberto (Vencidas e a Vencer)')
selecionar_opcao(navegador, 'Em Atraso / Vencidas')
selecionar_opcao(navegador, 'Mês Atual')
selecionar_opcao(navegador, 'Pagas')
selecionar_opcao(navegador, 'Todas')


time.sleep(1000)