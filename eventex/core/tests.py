from django.test import TestCase


"""
2017/04/17
aula M2A10: O resgate do código não testado
Ederson
"""

#Classe é um senário de teste, pois herda o TestCase
class HomeTest(TestCase):
    
    def setUp(self):
        """  """
        
        #Criar uma variável na class(self)
        self.response = self.client.get('/')
    
    def test_get(self):
        """GET / must return status code 200 """
        self.assertEqual(200,self.response.status_code)
        
    def test_template(self):
        """Must use  index.html"""
        #response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')