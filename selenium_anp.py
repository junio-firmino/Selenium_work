from selenium import webdriver
from selenium.webdriver import ActionChains
from openpyxl import load_workbook
from time import sleep
from selenium.webdriver.support.ui import Select



class Anp:
    def __init__(self):
        self.brower = webdriver.Chrome(executable_path='C:\\Users\\Jrfirmino Planejados\\Downloads\\chromedriver')


class Abrir_site(Anp):
    def __init__(self,site):
        super().__init__()
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
        self.senha = senha
        self.brower.implicitly_wait(3)
        self.brower.find_element_by_xpath('//*[@id="txtEmail"]').send_keys(log)
        self.brower.find_element_by_xpath('//*[@id="pwdSenha"]').send_keys(senha)
        self.brower.find_element_by_xpath('//*[@id="sbmLogin"]').click()

    def navegar_tela_anp(self):
        acao = ActionChains(self.brower)
        peticionamento = self.brower.find_element_by_xpath('//*[@id="main-menu"]/li[4]/a')
        processo_novo = self.brower.find_element_by_xpath('//*[@id="main-menu"]/li[4]/ul/li[1]/a')
        self.brower.implicitly_wait(3)
        acao.move_to_element(peticionamento).click()
        self.brower.implicitly_wait(5)
        acao.move_to_element(processo_novo).click().perform()
        self.brower.find_element_by_xpath('//*[@id="tblTipoProcedimento"]/tbody/tr[40]/td/a').click()

    def preencher_form(self):
        self.brower.find_element_by_xpath('//*[@id="txtEspecificacao"]').send_keys('2 Aditivo 4002079191 (AIR-BP Petro Bahia)')  #Primeira descrição
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
        self.brower.switch_to.frame(path.send_keys('C://Users//Jrfirmino Planejados//PycharmProjects//Aprendizado//teste_anp//Carta Externa Air BPPetrobahia.pdf'))
        self.brower.find_element_by_xpath('//*[@id="complementoPrincipal"]').send_keys('Carta Externa Air BPPetrobahia')
        choice_options = self.brower.find_element_by_xpath('//*[@id="nivelAcesso1"]')
        choice_options_elem = Select(choice_options)
        choice_options_elem.select_by_visible_text('Restrito')
        sleep(1)
        choice_options_2 = self.brower.find_element_by_xpath('//*[@id="hipoteseLegal1"]')
        choice_options_elem_2 = Select(choice_options_2)
        choice_options_elem_2.select_by_value('19')
        self.brower.find_element_by_xpath('//*[@id="rdNato1_1"]').click()
        self.brower.find_element_by_xpath('//*[@id="camposDigitalizadoPrincipalBotao"]/input').click()

    def escolher_frame1_contract(self):
        arquivo = ['202011_QAV-1_Segundo_Aditivo_Air_BPPB_4002079191_pdf.zip','202011_QAV-1_Segundo_Aditivo_Air_BPPB_4002079191.pdf']
        for arquivos in arquivo:
            path_2 = self.brower.find_element_by_xpath('//*[@id="fileArquivoComplementar"]')    #Button choice files
            self.brower.switch_to.frame(path_2.send_keys('C://Users//Jrfirmino Planejados//PycharmProjects//Aprendizado//teste_anp//'+arquivos))
            choice_options_frame1_contract = self.brower.find_element_by_xpath('//*[@id="tipoDocumentoComplementar"]')  #button drop-down
            choice_options_frame1_contract_elem = Select(choice_options_frame1_contract)
            choice_options_frame1_contract_elem.select_by_value('37')   #Choice button drop-down
            self.brower.find_element_by_xpath('//*[@id="complementoComplementar"]').send_keys(arquivos)
            choice_options_frame1_level = self.brower.find_element_by_xpath('//*[@id="nivelAcesso3"]')
            choice_options_frame1_level_elem = Select(choice_options_frame1_level)
            choice_options_frame1_level_elem.select_by_visible_text('Restrito')
            choice_options_frame1_level_hypothesis = self.brower.find_element_by_xpath('//*[@id="hipoteseLegal3"]')
            self.brower.implicitly_wait(1)
            choice_options_frame1_level_hypothesis_elem = Select(choice_options_frame1_level_hypothesis)
            choice_options_frame1_level_hypothesis_elem.select_by_value('19')
            self.brower.find_element_by_xpath('//*[@id="rdNato3_1"]').click()
            self.brower.find_element_by_xpath('//*[@id="camposDigitalizadoComplementarBotao"]/input').click()
            sleep(3)

    def final_form(self):
        self.brower.find_element_by_xpath('//*[@id="Peticionar"]').click()
        new_page_final = self.brower.window_handles
        for handle_final in new_page_final:
            self.brower.switch_to.window(handle_final)

        choice_page_final = self.brower.find_element_by_xpath('//*[@id="selCargo"]')
        choice_page_final_elem = Select(choice_page_final)
        choice_page_final_elem.select_by_value('118')
        self.brower.find_element_by_xpath('//*[@id="pwdsenhaSEI"]').send_keys(self.senha)
        print('Sucesso!!!')

    def download_receipt(self):
        self.brower.find_element_by_xpath('//*[@id="main-menu"]/li[5]/a').click()


if __name__ == '__main__':
    x= Navegar('http://www.anp.gov.br/')
    x.login()
    # x.navegar_tela_anp()
    # x.preencher_form()
    # x.escolher_frame1()
    # x.escolher_frame1_contract()
    # x.final_form()
    x.download_receipt()

