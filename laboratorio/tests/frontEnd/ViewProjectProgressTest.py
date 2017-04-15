from unittest import TestCase
from selenium import webdriver
import time

class ViewProjectProgressTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_add_progress(self):
        self.browser.get('http://localhost:8000/laboratorio')
        self.do_login()
        self.go_to_project_progress()
        self.add_progress()



    def go_to_project_progress(self):
        linkProjects = self.browser.find_element_by_id('linkProjects')
        linkProjects.click()
        time.sleep(5)
        linkReport = self.browser.find_element_by_id('report_1')
        linkReport.click()
        time.sleep(2)
        self.assertEqual('Laboratorio Uniandes', self.browser.title)

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

    def add_progress(self):
        totalReportedProgressBeforeSave = self.browser.find_element_by_id('counterProgress').get_attribute("value")

        btnAddProgress = self.browser.find_element_by_id('btnAddProgress')
        btnAddProgress.click()

        progress = self.browser.find_element_by_id('projectProgress')
        progress.send_keys('20')

        comment = self.browser.find_element_by_id('comment')
        comment.send_keys('avance del proyecto')

        btnSave = self.browser.find_element_by_id('btnSave')
        btnSave.click()

        btnReturn = self.browser.find_element_by_id('btnReturn')
        btnReturn.click()

        totalReportedProgressAfterSave = self.browser.find_element_by_id('counterProgress').get_attribute("value")

        self.assertEqual(totalReportedProgressAfterSave, totalReportedProgressBeforeSave+1)