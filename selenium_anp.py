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
        new_page = self.brower.window_handles
        for handle in new_page:
            self.brower.switch_to.window(handle)

    def login (self, log, senha):
        self.brower.implicitly_wait(1)
        self.brower.find_element_by_xpath('//*[@id="txtEmail"]').send_keys(log)
        self.brower.find_element_by_xpath('//*[@id="pwdSenha"]').send_keys(senha)
        self.brower.find_element_by_xpath('//*[@id="sbmLogin"]').click()
        self.brower.find_element_by_xpath('//*[@id="lnkSairSistema"]/img').click()
        self.brower.quit()


if __name__ == '__main__':
   x=Navegar('http://www.anp.gov.br/')
   x.login()
