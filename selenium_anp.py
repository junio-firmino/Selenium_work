from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Anp:
    def __init__(self):
        self.brower = webdriver.Firefox(executable_path='C:\\Users\\Jrfirmino Planejados\\Downloads\\geckodriver')

    def abrir_site(self):
        self.brower.get("http://www.anp.gov.br/")
        self.brower.implicitly_wait(40)

    def navegar(self):
        self.abrir_site()
        self.brower.maximize_window()
        self.brower.find_element_by_link_text('Processo Eletrônico (SEI)').click()
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_css_selector('.item-page > p:nth-child(18) > a:nth-child(1)').click()
        user = self.brower.find_element_by_id("txtEmail")
        print(user.is_displayed())
        print(user.is_enabled())
       # self.brower.find_element_by_xpath('').click()  # Usuário externo
    #  #self.logins()
    #  self.brower.implicitly_wait(40)
    #  x = self.brower.find_element_by_class_name("has-submenu")
    #  drp = Select(x)
    #  drp.select_by_visible_text('Processo Novo')
    #  #self.brower.find_element_by_link_text('Processo Novo').click()
    #  self.brower.implicitly_wait(5)
    #  self.brower.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/form/button').click()
    #  sleep(5)
    #  self.brower.close()

    def logins(self):
        self.brower.find_element_by_xpath("//*[@id='login_field']").send_keys('jrf.petro@gmail.com')
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_xpath("//*[@id='password']").send_keys('*j182928')
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_name('commit').click()

        # login = WebDriverWait(self.brower,20).until(EC.presence_of_element_located((By.ID,'txtEmail')))
        # login.send_keys('junio_firmino@petrobras.com.br')
        # login_senha = self.brower.find_element_by_id("pwdSenha")
        # login_senha.send_keys('j18m12jp29')
        # sleep(1)
        # comit = self.brower.find_element_by_css_selector('#sbmLogin')


x = Anp()
x.navegar()