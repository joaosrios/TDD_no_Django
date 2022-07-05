from django.test import TestCase, RequestFactory
from animais.models import Animal

class AnimalModelTestCase(TestCase):

    def setUp(self):
        self.animal = Animal.objects.create(
            nome_animal = "Leão",
            predador = "Sim",
            venenoso = "Não",
            domestico = "Não"
        )

    def test_animal_cadastrado_tem_caracteristicas(self):
        """Testa se animal está cadastrado com suas caracteristicas"""
        self.assertEqual(self.animal.nome_animal, "Leão")