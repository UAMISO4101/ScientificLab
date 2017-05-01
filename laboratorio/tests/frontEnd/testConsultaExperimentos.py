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

    def test_add_progress(self):
        self.browser.get('http://localhost:8000/laboratorio')
        self.do_login()

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

        link = self.browser.find_element_by_id('linkProjects')
        link.click()
        time.sleep(3)
        link = self.browser.find_element_by_xpath('//*[@id="myTable"]/tbody/tr[1]/td[6]/a[2]')
        link.click()
        time.sleep(3)



