from selenium import webdriver
from selenium.webdriver.firefox import service
from time import sleep
from selenium.webdriver.common.by import By
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
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_css_selector('.item-page > p:nth-child(19) > a:nth-child(1) > img:nth-child(1)').click()
        # user = self.brower.find_element_by_name('txtEmail')
        # user.send_keys('jrfirmino')
        # print(user.is_displayed())
        # print(user.is_enabled())
       # self.brower.find_element_by_xpath('').click()  # Usuário externo

        #  self.brower.implicitly_wait(40)
        #  x = self.brower.find_element_by_class_name("has-submenu")
        #  drp = Select(x)
        #  drp.select_by_visible_text('Processo Novo')
        #  #self.brower.find_element_by_link_text('Processo Novo').click()
        #  self.brower.implicitly_wait(5)
        #  self.brower.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/form/button').click()
        #  sleep(5)
        #  self.brower.close()

class Logins(Anp):
    def __init__(self,site):
        super().__init__(site)
        self.brower.implicitly_wait(5)
        WebDriverWait(self.brower, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#txtEmail'))).send_keys('')
        #self.brower.find_element_by_css_selector('#txtEmail').send_keys('jrf.petro@gmail.com')
        self.brower.find_element_by_xpath("//*[@id='password']").send_keys('')
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_name('commit').click()

        # login = WebDriverWait(self.brower,20).until(EC.presence_of_element_located((By.ID,'txtEmail')))
        # login.send_keys('junio_firmino@.com.br')
        # login_senha = self.brower.find_element_by_id("pwdSenha")
        # login_senha.send_keys('j18m12jp29')
        # sleep(1)
        # comit = self.brower.find_element_by_css_selector('#sbmLogin')


if __name__ == '__main__':
   x=Navegar('http://www.anp.gov.br/')
   y=Logins('http://www.anp.gov.br/')
