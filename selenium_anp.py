from selenium import webdriver
from selenium.webdriver.firefox import service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Anp:
    def __init__(self, site):
        self.brower = webdriver.Chrome(executable_path='C:\\Users\\Jrfirmino Planejados\\Downloads\\chromedriver')
        self.site = site

class Abrir_site(Anp):
    def __init__(self,site):
        super().__init__(site)
        self.brower.get(site)
        self.brower.implicitly_wait(5)


class Navegar(Abrir_site):
    def __init__(self,site):
        super().__init__(site)
        self.brower.maximize_window()
        self.brower.find_element_by_link_text('Processo Eletrônico (SEI)').click()
        self.brower.find_element_by_css_selector('.item-page > p:nth-child(19) > a:nth-child(1) > img:nth-child(1)').click()
        self.brower.implicitly_wait(5)
        #self.brower.close()
        self.brower.get('https://sei.anp.gov.br/sei/controlador_externo.php?acao=usuario_externo_logar&id_orgao_acesso_externo=0')
        self.brower.find_element_by_xpath('//*[@id="txtEmail"]').send_keys('')
        self.brower.find_element_by_xpath('//*[@id="pwdSenha"]').send_keys('')
        self.brower.find_element_by_xpath('//*[@id="sbmLogin"]').click()







class Logins(Anp):
    def __init__(self,site):
        super().__init__(site)

        # self.brower.implicitly_wait(5)
        # #self.brower.close()
        # self.brower.find_element_by_tag_name('html').send_keys(Keys.TAB)
        # #self.brower.get("https://sei.anp.gov.br/sei/controlador_externo.php?acao=usuario_externo_logar&id_orgao_acesso_externo=0")
        # WebDriverWait(self.brower, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "infraText"))).send_keys('jjeo')
        # #self.brower.find_element_by_id("txtEmail").send_keys('jrf.petro@gmail.com')
        # self.brower.find_element_by_xpath("//*[@id='password']").send_keys('')
        # self.brower.implicitly_wait(5)
        # self.brower.find_element_by_name('commit').click()

        # login = WebDriverWait(self.brower,20).until(EC.presence_of_element_located((By.ID,'txtEmail')))
        # login.send_keys('junio_firmino@.com.br')
        # login_senha = self.brower.find_element_by_id("pwdSenha")
        # login_senha.send_keys('')
        # sleep(1)
        # comit = self.brower.find_element_by_css_selector('#sbmLogin')


if __name__ == '__main__':
   x=Navegar('http://www.anp.gov.br/')
   #y=Logins('http://www.anp.gov.br/')
