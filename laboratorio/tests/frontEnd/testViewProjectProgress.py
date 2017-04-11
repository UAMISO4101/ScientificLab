from django.test import LiveServerTestCase
from selenium import webdriver


class testViewProjectProgress(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.baseUrl = self.live_server_url + '/laboratorio/';
        self.nombreUsuario = 'usuarioprueba';
        self.nombre = 'Usuario Prueba';
        self.password = 'agiles123';

    def tearDown(self):
        self.browser.quit()

