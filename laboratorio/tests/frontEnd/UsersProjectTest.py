from unittest import TestCase
from selenium import webdriver
import time
import random
from selenium.webdriver.support.select import Select


class UsersProjectTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000/laboratorio')
        self.do_login()
        self.assertIn('Laboratorio Uniandes',self.browser.title)

    def test_links_project_Users(self):
        self.browser.get('http://localhost:8000/laboratorio')
        self.do_login()
        linkProjects = self.browser.find_element_by_id('linkProjects')
        linkProjects.click()
        time.sleep(4)
        numProject = self.Rows_table_Project()
        print(numProject)
        i = 0
        while i < numProject:
            linkProjectSel = "Users_" + str(random.randint(1, numProject))
            linkUsers = self.browser.find_element_by_id(linkProjectSel)
            linkUsers.click()
            time.sleep(2)
            tableUser = self.browser.find_element_by_id('listUserProject')
            tableUser.click()
            self.browser.execute_script("window.history.go(-1)")
            time.sleep(2)
            i+=3

    def test_go_to_project_Users(self):
        self.browser.get('http://localhost:8000/laboratorio')
        self.do_login()
        linkProjects = self.browser.find_element_by_id('linkProjects')
        linkProjects.click()
        time.sleep(4)
        #linkProjectSel = "Users_" + str(random.randint(1, self.Rows_table_Project()))
        #linkUsers = self.browser.find_element_by_id(linkProjectSel)
        linkUsers = self.browser.find_element_by_id('Users_4')
        linkUsers.click()
        time.sleep(2)
        print(self.Rows_table_Users())
        titlePage = self.browser.find_element_by_id('titlePage').text
        titleProject = self.browser.find_element_by_id('titleProject').text
        print(titlePage)
        self.assertEqual('USUARIOS DEL PROYECTO: ' + titleProject, titlePage)
        time.sleep(2)

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
        return self.browser.execute_script("return document.getElementsByTagName('tr').length") - 3

    def Rows_table_Users(self):
        return self.browser.execute_script("return document.getElementsByTagName('tr').length") - 1
