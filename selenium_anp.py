from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox import service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Anp:
    def __init__(self):
        self.brower = webdriver.Chrome(executable_path='C:\\Users\\Jrfirmino Planejados\\Downloads\\chromedriver')

    def site_1(self,site):
        self.site = site


class Abrir_site(Anp):
    def __init__(self,site):
        super().__init__()
        super().site_1(site)
        self.brower.get(site)
        self.brower.implicitly_wait(5)


class Navegar(Abrir_site):
    def __init__(self,site):
        super().__init__(site)
        self.brower.maximize_window()
        self.brower.find_element_by_link_text('Processo Eletrônico (SEI)').click()
        self.brower.find_element_by_xpath('//*[@id="content-section"]/div[1]/div[1]/p[10]/a/img').click()
        self.brower.implicitly_wait(5)
        new_page = self.brower.window_handles
        for handle in new_page:
            self.brower.switch_to.window(handle)

    def login (self, log, senha):
        self.brower.implicitly_wait(1)
        self.brower.find_element_by_xpath('//*[@id="txtEmail"]').send_keys(log)
        self.brower.find_element_by_xpath('//*[@id="pwdSenha"]').send_keys(senha)
        self.brower.find_element_by_xpath('//*[@id="sbmLogin"]').click()
        #self.brower.find_element_by_xpath('//*[@id="lnkSairSistema"]/img').click()
        #self.brower.quit()
        peticionamento = self.brower.find_element_by_xpath('//*[@id="main-menu"]/li[4]/a')
        processo_novo = self.brower.find_element_by_xpath('//*[@id="main-menu"]/li[4]/ul/li[1]/a')
        acao = ActionChains(self.brower)
        acao.move_to_element(peticionamento).perform()
        self.brower.implicitly_wait(1)
        acao.move_to_element(processo_novo).click().perform()
        self.brower.find_element_by_xpath('//*[@id="tblTipoProcedimento"]/tbody/tr[40]/td/a').click()


class Navegar_tela_anp(Anp):
    def __init__(self):
        super().__init__()

    def escolha_tela(self):
        #self.brower.get('https://sei.anp.gov.br/sei/controlador_externo.php?acao=usuario_externo_controle_acessos&acao_origem=usuario_externo_logar&id_orgao_acesso_externo=0&infra_hash=4162e975342b0dca317d40c61679bfa7')
        pass



if __name__ == '__main__':
    x= Navegar('http://www.anp.gov.br/')
    x.login()
