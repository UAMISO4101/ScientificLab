# -*- coding: utf-8 -*-
import random
from unittest import TestCase
import time
import sys
from selenium import webdriver
from selenium.webdriver.support.select import Select

class FunctionalTest(TestCase):

    def setUp(self):
        self.browser= webdriver.Chrome()
        self.baseUrl = 'http://localhost:8000/laboratorio'

    #def tearDown(self):
        #self.browser.quit()

    def atest_title(self):
        self.browser.get(self.baseUrl)
        self.assertIn('Laboratorio Uniandes', self.browser.title)

    def test_login(self):
        # Crear el usuario
        self.browser.get(self.baseUrl)
        self.browser.implicitly_wait(10)

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

        link = self.browser.find_element_by_id('linkProtocolos')
        link.click()
        time.sleep(3)

        link = self.browser.find_element_by_id('linkAgregarProtocolo')
        link.click()
        time.sleep(3)

        element = self.browser.find_element_by_id('titulo')
        element.send_keys('Protocolo Prueba')

        element = Select(self.browser.find_element_by_id('categoria'))
        element.select_by_index(1)

        element = self.browser.find_element_by_id('habilitado')
        element.click()

        element = self.browser.find_element_by_xpath('//div[@class="jqte_editor"]')
        element.send_keys('Protocolo Prueba')

        botonGuardar = self.browser.find_element_by_id('btn_guardar')
        botonGuardar.click()
        self.browser.implicitly_wait(3)
        time.sleep(2)
