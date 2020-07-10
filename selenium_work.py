from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Anp:
    def __init__(self):
        self.brower = webdriver.Firefox(executable_path='C:\\Users\\Jrfirmino Planejados\\Downloads\\geckodriver')

    def abrir_site(self):
        self.brower.get("http://www.anp.gov.br/")
        sleep(1)

    def navegar(self):
        self.abrir_site()
        pro_sei = self.brower.find_element_by_link_text('Processo Eletrônico (SEI)')
        pro_sei.click()
        acesso = self.brower.find_element_by_css_selector('.item-page > p:nth-child(18) > a:nth-child(1) > img:nth-child(1)')
        acesso.click()
        self.logins()

    def logins(self):

        login= self.brower.find_elements(By.XPATH,'//*[@id="txtEmail"]')
        print(len(login))
        #login = WebDriverWait(self.brower,20).until(EC.presence_of_element_located((By.ID,'txtEmail')))
        # login.send_keys('')
        # login_senha = self.brower.find_element_by_id("pwdSenha")
        # login_senha.send_keys('')
        # sleep(1)
        # comit = self.brower.find_element_by_css_selector('#sbmLogin')

x = Anp()
x.navegar()
    #brower.close()
0
