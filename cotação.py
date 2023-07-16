import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Chrome()

#COTAÇÃO DOLAR

navegador.get('https://www.linkedin.com')
navegador.find_element('xpath','//*[@id="session_key"]').send_keys('andrepontesvazdemedeiros@gmail.com')
navegador.find_element('xpath','//*[@id="session_password"]').send_keys('ozana007')
navegador.find_element('xpath','//*[@id="session_password"]').send_keys(Keys.ENTER)



#navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys('Cotação dólar')
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

#COTAÇÃO EURO

navegador.get('https://www.google.com.br/')
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys('Cotação euro')
navegador.find_element('xpath','//*[@id="APjFqb"]').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath','//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

#COTAÇÃO OURO

navegador.get('https://www.melhorcambio.com/ouro-hoje')
cotacao_ouro = navegador.find_element('xpath','//*[@id="comercial"]').get_attribute('value').replace(',','.')
print(cotacao_ouro)

navegador.quit()