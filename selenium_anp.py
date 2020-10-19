from selenium import webdriver
from selenium.webdriver import ActionChains
from openpyxl import load_workbook
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


class Anp:
    #site = input('qual site? ')
    def __init__(self):
        self.brower = webdriver.Chrome(executable_path='C:\\Users\\Jrfirmino Planejados\\Downloads\\chromedriver')

    def site_1(self,site):
        self.site = site
        pass


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
        self.brower.implicitly_wait(1)
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

    def navegar_tela_anp(self):
        acao = ActionChains(self.brower)
        peticionamento = self.brower.find_element_by_xpath('//*[@id="main-menu"]/li[4]/a')
        processo_novo = self.brower.find_element_by_xpath('//*[@id="main-menu"]/li[4]/ul/li[1]/a')
        sleep(3)
        #self.brower.implicitly_wait(3)
        acao.move_to_element(peticionamento).perform()
        self.brower.implicitly_wait(2)
        acao.move_to_element(processo_novo).click().perform()
        self.brower.find_element_by_xpath('//*[@id="tblTipoProcedimento"]/tbody/tr[40]/td/a').click()

    def preencher_form(self):
        self.brower.find_element_by_xpath('//*[@id="txtEspecificacao"]').send_keys('contrato teste')
        self.brower.find_element_by_xpath('//*[@id="optTipoPessoaJuridica"]').click()
        self.brower.find_element_by_xpath('//*[@id="optTipoPessoaJuridica"]').is_selected()
        cnpj = [33000167000101,22899533000190]
        for cnpjs in cnpj:
            self.brower.find_element_by_xpath('//*[@id="txtCNPJ"]').send_keys(cnpjs)
            self.brower.find_element_by_xpath('//*[@id="btValidarCPFCNPJ"]').click()
            sleep(3)
            self.brower.find_element_by_xpath('//*[@id="btAdicionarInteressado"]').click()

    def escolher_frame1(self):
        path = self.brower.find_element_by_xpath('//*[@id="fileArquivoPrincipal"]')
        self.brower.switch_to.frame(path.send_keys('C://Users/Jrfirmino Planejados/PycharmProjects/Aprendizado/hello.txt'))
        self.brower.find_element_by_xpath('//*[@id="complementoPrincipal"]').send_keys('Carta externas')
        choice_options = self.brower.find_element_by_xpath('//*[@id="nivelAcesso1"]')
        choice_options_elem = Select(choice_options)
        choice_options_elem.select_by_visible_text('Restrito')
        sleep(1)
        choice_options_2 = self.brower.find_element_by_xpath('//*[@id="hipoteseLegal1"]')
        choice_options_elem_2 = Select(choice_options_2)
        choice_options_elem_2.select_by_value('19')
        self.brower.find_element_by_xpath('//*[@id="rdNato1_1"]').click()
        self.brower.find_element_by_xpath('//*[@id="optTipoPessoaJuridica"]').is_selected()
        self.brower.find_element_by_xpath('//*[@id="camposDigitalizadoPrincipalBotao"]/input').click()

    def escolher_frame1_contract(self):
        path_2 = self.brower.find_element_by_xpath('//*[@id="fileArquivoComplementar"]')


if __name__ == '__main__':
    x= Navegar('http://www.anp.gov.br/')
    x.login('')
    x.navegar_tela_anp()
    x.preencher_form()
    x.escolher_frame1()
