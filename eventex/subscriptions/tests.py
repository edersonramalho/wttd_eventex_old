from django.test import TestCase
from django.core.handlers.exception import response_for_exception
from eventex.subscriptions.forms import SubscriptionForm
from django.core import mail
from symbol import subscript

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

class SubscribePostTest(TestCase):
    def setUp(self):
        data = dict(name='Ederson da Silva Santos', cpf='12345678901',
                    email='edersonramalho@gmail.com', phone='27-998310978')
        self.resp = self.client.post('/inscricao/', data)
        
    def test_post(self):
        """ Teste de redirecionamento para /inscricao/ (POST) """
        
        #302 é o codi do redirecionamento
        self.assertEqual(302, self.resp.status_code)
        
    def test_send_subscribe_email(self):
        """ Teste de Envio de e-mail """
        #Verifica se foi enviado 1 e-mail, o este não envia e-mail
        self.assertEqual(1, len(mail.outbox))
        
    def test_subscription_email_subject(self):
        email = mail.outbox[0]
        esperado = 'Confirmação de inscrição'
        
        self.assertEqual(esperado, email.subject) 
        
    def test_subscription_email_from(self):
        email = mail.outbox[0]
        esperado = 'contato@eventex.com.br'
        
        self.assertEqual(esperado, email.from_email)
    
    def test_subscription_email_to(self):
        email = mail.outbox[0]
        esperado = ['contato@eventex.com.br','edersonramalho@gmail.com']
        
        self.assertEqual(esperado, email.to)
        
    def test_subscription_email_body(self):
        email = mail.outbox[0]
        
        self.assertIn('Ederson da Silva Santos', email.body)
        self.assertIn('edersonramalho@gmail.com', email.body)
        self.assertIn('12345678901', email.body)
        self.assertIn('27-998310978', email.body)
        
class SubscribeInvalidPost(TestCase):
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


