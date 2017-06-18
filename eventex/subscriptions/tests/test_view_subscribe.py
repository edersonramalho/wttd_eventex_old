from django.test import TestCase
from django.core import mail
#from django.core.handlers.exception import response_for_exception
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeGet(TestCase):
    
    def setUp(self):
        self.resp = self.client.get('/inscricao/')
    
    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)
    
    def test_subscription(self):
        """Must user subscriptions/subscription_form.html"""         
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
        
    def test_html(self):
        """Testa os imputs do Html"""
        
        tags = (('<form',1),
                ('<input',6),
                ('type="text"',3),
                ('type="email"',1),
                ('type="submit"',1))
        
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

        
    def test_csrf(self):
        """
        Verifica se existe um CSRF no form, 
        que é um item obrigatório em todo form  Django
        Um mecanismo de segurança no Django 
        """
        self.assertContains(self.resp, 'csrfmiddlewaretoken')
        #O Django gera um token em modo de execução {% csrf_token %} dentro do Form
    
        
    def test_has_form(self):
        """ Verificar se existe contexto Form """
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostvalid(TestCase):
    def setUp(self):
        data = dict(name='Ederson da Silva Santos', cpf='12345678901',
                    email='edersonramalho@gmail.com', phone='27-998310978')
        self.resp = self.client.post('/inscricao/', data)
        
    def test_post(self):
        """ Teste de redirecionamento para /inscricao/1/ (POST) """
        self.assertRedirects(self.resp, '/inscricao/1/')
    
    #def test_post(self):
    #    """ Teste de redirecionamento para /inscricao/ (POST) """
    #    
    #    #302 é o codi do redirecionamento
    #    self.assertEqual(302, self.resp.status_code)
    
    def test_send_subscribe_email(self):
        """ Teste de Envio de e-mail """
        #Verifica se foi enviado 1 e-mail, o este não envia e-mail
        self.assertEqual(1, len(mail.outbox))
        
    def test_save_subscription(self):
        self.assertTrue(Subscription.objects.exists())        
        
class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})
        
    def test_post(self):
        """ Verifica se o o form esta retornando fom form invalid e valid """                
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')
        
    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)
    
    def test_form_has_errors(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)
    
    def test_dont_save_subscription(self):
        self.assertFalse(Subscription.objects.exists())



