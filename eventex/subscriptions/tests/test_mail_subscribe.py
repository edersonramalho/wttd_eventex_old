from django.test import TestCase
from django.core import mail


class SubscribePostvalid(TestCase):
    def setUp(self):
        data = dict(name='Ederson da Silva Santos', cpf='12345678901',
                    email='edersonramalho@gmail.com', phone='27-998310978')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
            
    def test_subscription_email_subject(self):        
        esperado = 'Confirmação de inscrição'        
        self.assertEqual(esperado, self.email.subject) 
        
    def test_subscription_email_from(self):        
        esperado = 'contato@eventex.com.br'        
        self.assertEqual(esperado, self.email.from_email)
    
    def test_subscription_email_to(self):        
        esperado = ['contato@eventex.com.br','edersonramalho@gmail.com']        
        self.assertEqual(esperado, self.email.to)
        
    def test_subscription_email_body(self):
        
        texts = ('Ederson da Silva Santos',
                'edersonramalho@gmail.com',
                '12345678901',
                '27-998310978')
        for text in texts:
            with self.subTest():
                self.assertIn(text, self.email.body)