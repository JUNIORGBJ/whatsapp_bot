from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
# Abrir o Whatsapp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com')
while len(driver.find_elements_by_id("side")) <1:
    time.sleep(1)
# Contatos ou grupos e mensagem a ser enviada
contatos = ['Junior Links','Aline Airão']
mensagem = 'Boa noite Grupo, Agora está funcionando filé'
# Buscar contatos ou grupos
def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(2)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)
 # Enviar a mensagem para o contato ou grupo   
def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(2)
    campo_mensagem[1].send_keys(mensagem)
    time.sleep(2)
    campo_mensagem[1].send_keys(Keys.ENTER)
for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
