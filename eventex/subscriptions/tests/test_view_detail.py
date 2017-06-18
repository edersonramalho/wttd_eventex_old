from django.test import TestCase
from eventex.subscriptions.models import Subscription



#Cenário de sucesso
class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Ederson da Silva Santos',
            email='edersonramalho@gmail.com',
            cpf='12345678901',
            phone='27-998310978'
            )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))
    
    def test_get(self):        
        self.assertEqual(200,self.resp.status_code)
        
    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_detail.html')
    
    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription )
        
    def test_html(self):
        
        contents = (self.obj.name, self.obj.email, self.obj.cpf, self.obj.phone) 
        #('Ederson da Silva Santos','edersonramalho@gmail.com','12345678901','27-998310978')
        
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)        

#Cenário de falha
class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)