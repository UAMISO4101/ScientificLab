from unittest import TestCase
from selenium import webdriver
import time
import random

class DetailsProtocolTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)
        self.baseUrl = 'http://localhost:8000/laboratorio'

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get(self.baseUrl)
        self.do_login()
        self.assertIn('Laboratorio Uniandes', self.browser.title)

    def test_links_protocolo_details(self):
        self.browser.get(self.baseUrl)
        self.do_login()
        time.sleep(2)

        linkProtocolo = self.browser.find_element_by_id('linkProtocolos')
        linkProtocolo.click()

        time.sleep(6)
        numProtocolos = self.Rows_table_Protocolo()
        i = 0

        while i < numProtocolos:
            linkProtocoloSel = self.find_linkProtocoloSel(numProtocolos)
            linkUsers = self.browser.find_element_by_id(linkProtocoloSel)
            linkUsers.click()
            time.sleep(4)
            BtnRegresar = self.browser.find_element_by_id('Btn_Regresar')
            BtnRegresar.click()
            time.sleep(6)
            i+=3

    def test_go_to_protocolo_details(self):
        self.browser.get(self.baseUrl)
        self.do_login()
        time.sleep(2)

        linkProtocolo = self.browser.find_element_by_id('linkProtocolos')
        linkProtocolo.click()
        time.sleep(6)

        numProtocolos = self.Rows_table_Protocolo()
        linkProtocoloSel = self.find_linkProtocoloSel(numProtocolos)
        linkUsers = self.browser.find_element_by_id(linkProtocoloSel)
        linkUsers.click()
        time.sleep(3)

        titlePage = self.browser.find_element_by_id('titlePage').text
        self.assertEqual("DETALLE DE PROTOCOLO", titlePage)

        ProtocoloId = self.browser.find_element_by_id("ProtocoloID").get_attribute("value")
        #protocolo = Protocolo.objects.get(id=ProtocoloId)

        ReadOnly = self.browser.find_element_by_id("titulo").get_attribute("disabled")
        self.assertEqual("true", str(ReadOnly))
        ReadOnly = self.browser.find_element_by_id("version").get_attribute("disabled")
        self.assertEqual("true", str(ReadOnly))
        ReadOnly = self.browser.find_element_by_id("categoria").get_attribute("disabled")
        self.assertEqual("true", str(ReadOnly))

        ReadOnly = self.browser.find_element_by_id("habilitado").get_attribute("readonly")
        self.assertEqual("true", str(ReadOnly))
        habilitado = self.browser.find_element_by_id("habilitado").get_attribute("checked")
        val_habilitado = self.browser.find_element_by_id("val_habilitado").get_attribute("value")
        if habilitado:
            self.assertEqual("True", val_habilitado)
        else:
            self.assertNotEqual("True", val_habilitado)

        ReadOnly = self.browser.find_element_by_id("descripcion").get_attribute("disabled")
        self.assertEqual("true", str(ReadOnly))

    def find_linkProtocoloSel(self, numRows):
        continuar = True
        while continuar:
            try:
                linkProtocolo = "Details_" + str(random.randint(1, numRows))
                self.browser.find_element_by_id(linkProtocolo)
                continuar = False
            except:
                continuar = True
        return linkProtocolo

    def do_login(self):
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

    def Rows_table_Protocolo(self):
        return self.browser.execute_script("return document.getElementsByTagName('tr').length") - 1