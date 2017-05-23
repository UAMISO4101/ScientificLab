from unittest import TestCase
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class testConsultaExperimentos(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_Resultado(self):
        self.browser.get('http://localhost:8000/laboratorio')
        self.do_login()
        self.create_poject()
        self.create_experiment()
        self.edit_experiment()
        self.colsultar_experiment()

    def do_login(self):
        link = self.browser.find_element_by_id('link_iniciar_sesion')
        link.click()
        time.sleep(3)

        element = self.browser.find_element_by_id('username')
        element.send_keys('test')

        clave = self.browser.find_element_by_id('password')
        clave.send_keys('agiles123')

        btn = self.browser.find_element_by_id('btn_iniciar_sesion')
        btn.click()
        time.sleep(3)

    def create_poject(self):
        linkProjects = self.browser.find_element_by_id('linkProjects')
        linkProjects.click()
        time.sleep(3)
        linkReport = self.browser.find_element_by_xpath('//*[@id="portfolio"]/div/a')
        linkReport.click()
        time.sleep(3)

        element = self.browser.find_element_by_id('nombre')
        element.send_keys('1 - Test Resultado Experimento')

        element = self.browser.find_element_by_id('fechaInicio')
        element.send_keys('2017-10-31')

        element = self.browser.find_element_by_id('fechaFinal')
        element.send_keys('2017-12-31')

        element = Select(self.browser.find_element_by_id('patrocinador'))
        element.select_by_index(1)

        element = Select(self.browser.find_element_by_id('estado'))
        element.select_by_index(2)

        element = self.browser.find_element_by_id('prioridad')
        element.send_keys('1')

        element = self.browser.find_element_by_id('descripcion')
        element.send_keys('Test Resultado Experimento descripcion')

        element = self.browser.find_element_by_xpath('//*[@id="formProject"]/div[8]/input')
        element.click()
        time.sleep(3)

        element = self.browser.find_element_by_xpath('//*[@id="formProject"]/div[8]/a')
        element.click()
        time.sleep(3)

    def create_experiment(self):
        element = self.browser.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[1]/td[6]/a[2]')
        element.click()
        time.sleep(3)

        element = self.browser.find_element_by_xpath('//*[@id="portfolio"]/div/a')
        element.click()
        time.sleep(3)

        element = self.browser.find_element_by_id('nombre')
        element.send_keys('Resultado Experimento 1')

        element = self.browser.find_element_by_id('fechaInicio')
        element.send_keys('2017-12-31')

        element = Select(self.browser.find_element_by_id('responsable'))
        element.select_by_index(1)

        element = Select(self.browser.find_element_by_id('estado'))
        element.select_by_index(2)

        element = self.browser.find_element_by_id('prioridad')
        element.send_keys('1')

        element = self.browser.find_element_by_id('descripcion')
        element.send_keys('Experimento extraccion de muestra exitosa')

        element = self.browser.find_element_by_xpath('//*[@id="formAddExperiment"]/div[8]/input')
        element.click()
        time.sleep(3)

        element = self.browser.find_element_by_xpath('//*[@id="formAddExperiment"]/div[8]/a')
        element.click()
        time.sleep(3)

    def edit_experiment(self):
        element = self.browser.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[1]/td[8]/a[1]')
        element.click()
        time.sleep(3)

        element = Select(self.browser.find_element_by_id('resultado'))
        element.select_by_index(1)

        element = self.browser.find_element_by_xpath('//*[@id="formEditExperiment"]/div[9]/input')

        element.click()
        time.sleep(3)

        element = self.browser.find_element_by_xpath('//*[@id="formEditExperiment"]/div[9]/a')
        element.click()
        time.sleep(3)

    def colsultar_experiment(self):
        element = self.browser.find_element_by_xpath('// *[ @ id = "myTable"] / tbody / tr[1] / td[8] / a[2]')
        element.click()
        time.sleep(3)

        resultado = self.browser.find_element_by_id('resultado').get_attribute("value")
        self.assertEqual((resultado), "Exitoso")
