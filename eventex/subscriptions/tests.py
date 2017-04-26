from django.test import TestCase
from django.core.handlers.exception import response_for_exception
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    
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
        self.assertContains(self.resp, '<form')
        #self.assertContains(self.resp, '<imput',5)
        #self.assertContains(self.resp, 'type="text"',3)
        #self.assertContains(self.resp, 'type="email"')
        #self.assertContains(self.resp, 'type="submit"')
        
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
        
    def test_form_has_fields(self):
        """ Tem que existir 04 campos """
        form = self.resp.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))
        
    
        