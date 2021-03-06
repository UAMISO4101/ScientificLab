from unittest import TestCase
from selenium import webdriver
import time
import random

class UsersProjectTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)
        self.baseUrl = 'http://localhost:8000/laboratorio'

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get(self.baseUrl)
        self.do_login()
        self.assertIn('Laboratorio Uniandes',self.browser.title)

    def test_links_project_Users(self):
        self.browser.get(self.baseUrl)
        self.do_login()
        time.sleep(2)

        linkProjects = self.browser.find_element_by_id('linkProjects')
        linkProjects.click()
        time.sleep(6)

        numProject = self.Rows_table_Project()
        i = 0
        while i < numProject:
            linkProjectSel = self.find_linkProjectSel(numProject)
            linkUsers = self.browser.find_element_by_id(linkProjectSel)
            linkUsers.click()
            time.sleep(4)
            tableUser = self.browser.find_element_by_id('listUserProject')
            tableUser.click()
            self.browser.execute_script("window.history.go(-1)")
            time.sleep(6)
            i+=3

    def test_go_to_project_Users(self):
        self.browser.get(self.baseUrl)
        self.do_login()
        time.sleep(2)

        linkProjects = self.browser.find_element_by_id('linkProjects')
        linkProjects.click()
        time.sleep(6)

        numProject = self.Rows_table_Project()
        linkProjectSel = self.find_linkProjectSel(numProject)
        linkUsers = self.browser.find_element_by_id(linkProjectSel)
        linkUsers.click()
        time.sleep(4)

        titlePage = self.browser.find_element_by_id('titlePage').text
        titleProject = self.browser.find_element_by_id('titleProject').get_attribute("value");
        self.assertEqual('USUARIOS DEL PROYECTO: ' + titleProject.upper(), titlePage)

    def find_linkProjectSel(self, numRows):
        continuar = True
        while continuar:
            try:
                linkProject = "Users_" + str(random.randint(1, numRows))
                self.browser.find_element_by_id(linkProject)
                continuar = False
            except:
                continuar = True
        return linkProject

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

    def Rows_table_Project(self):
        return self.browser.execute_script("return document.getElementsByTagName('tr').length") - 1

    def Rows_table_Users(self):
        return self.browser.execute_script("return document.getElementsByTagName('tr').length") - 1
