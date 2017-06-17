from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime


class SubscriptionModelCase(TestCase):
    
    def setUp(self):
        #em memória
        self.obj = Subscription(
                name="Ederson da Silva Santos",
                cpf="12345678901",
                email="edersonramalho@gmail.com",
                phone="27-998310978"                
            )
        #salvar em db
        self.obj.save()
    
    def test_create(self):
        self.assertTrue(Subscription.objects.exists(),'Não existe o objeto')
        
    def test_create_at(self):
        """ Subscription must have on auto create_at attr."""
        self.assertIsInstance(self.obj.create_at, datetime, "Erro no datetime do criação do obj")