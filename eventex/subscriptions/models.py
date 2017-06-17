from django.db import models

class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF',max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone',max_length=20)
    create_at = models.DateTimeField('criado em',auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'inscrições'        
        verbose_name = 'inscrição'
        ordering = ('-create_at',) # o "-" significa o desc
    
    def __str__(self):
        return self.name