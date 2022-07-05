from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from animais.models import Animal

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(r'C:\Users\joaos\Documents\Estudos\TDD no Django\tdd_busca_animal\chromedriver.exe')
        self.animal = Animal.objects.create(
            nome_animal = "Leão",
            predador = "Sim",
            venenoso = "Não",
            domestico = "Não"
        )

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """
        teste se o usuário enccontra um novo animal pesquisando
        """

        #Ele encontra o busca animal e decide usar o site
        home_page = self.browser.get(self.live_server_url + '/')
        #porque ele vê no menu do site escrito Busca Animal
        brand_element = self.browser.find_element(By.CSS_SELECTOR, '.navbar')
        self.assertEqual('Busca Animal', brand_element.text)

        #ele vê um campo para pesquisar animais pelo nome
        buscar_animal_input = self.browser.find_element(By.CSS_SELECTOR, 'input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão')

        #ele pesquisa por leão e clica no botão pesquisar
        buscar_animal_input.send_keys('leão')
        self.browser.find_element(By.CSS_SELECTOR, 'form button').click()

        #o site exibe 4 caracteristicas do animal pesquisado
        caracteristicas = self.browser.find_elements(By.CSS_SELECTOR, '.result-description')
        self.assertGreater(len(caracteristicas), 3)

