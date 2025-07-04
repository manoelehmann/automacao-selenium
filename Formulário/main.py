from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get('https://maxxsoft.com.br/site/')

navegador.maximize_window()

produto = navegador.find_elements('class name', 'e-n-menu-title-container')

for botao in produto:
    if 'Produtos' in botao.text:
        botao.click()
        break

time.sleep(1)

maxxrural = navegador.find_elements('class name', 'elementor-button-wrapper')
for botao in maxxrural:
    if 'Saiba mais' in botao.text:
        botao.click()
        break

                    # preenchimento de formulário

navegador.find_element('id', 'form-field-name').send_keys('Teste')
navegador.find_element('id', 'form-field-email').send_keys('teste@gmail.com')
navegador.find_element('id', 'form-field-field_d83a4c9').send_keys('goias')
navegador.find_element('id', 'form-field-field_7024397').send_keys('goiania')
navegador.find_element('id', 'form-field-field_177440f').send_keys('teste teste teste teste')

navegador.find_element('class name', 'elementor-button.elementor-size-sm.elementor-animation-grow').click()

'''navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})",
                         botao_enviar)'''
                         
                         
time.sleep(100)