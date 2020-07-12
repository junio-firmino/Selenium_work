from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Anp:
    def __init__(self):
        self.brower = webdriver.Firefox(executable_path='C:\\Users\\Jrfirmino Planejados\\Downloads\\geckodriver')

    def abrir_site(self):
        self.brower.get("https://github.com/")
        sleep(1)

    def navegar(self):
        self.abrir_site()
        self.brower.maximize_window()
        self.brower.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]").click()
        self.brower.implicitly_wait(5)
        self.logins()
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_css_selector('.js-feature-preview-indicator-container > summary:nth-child(1)').click()
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_xpath('/html/body/div[1]/header/div[7]/details/details-menu/form/button').click()
        sleep(5)
        self.brower.close()

    def logins(self):
        self.brower.find_element_by_xpath("//*[@id='login_field']").send_keys('')
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_xpath("//*[@id='password']").send_keys('')
        self.brower.implicitly_wait(5)
        self.brower.find_element_by_name('commit').click()

       
x = Anp()
x.navegar()

