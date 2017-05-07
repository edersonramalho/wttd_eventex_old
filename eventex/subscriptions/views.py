#from django.http.response import HttpResponse
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages

def subscribe(request):
    if (request.method == 'POST'):
        
#         context = dict(name='Ederson da Silva Santos', cpf='12345678901',
#                     email='edersonramalho@gmail.com', phone='27-998310978')

        # Pegar dados do Form, como String
        form = SubscriptionForm(request.POST) 
        #Transformar strings em Objetos python
        #form.full_clean()
        
        #o full_clean retorna erro se não existir os itens no form, logo é melhor usar o is_valid
        # o is valid execura internamento o full_clean e retorna true ou false se invalido.
        if (form.is_valid()):             
        
            body = render_to_string('subscriptions/subscription_email.txt',
                                    form.cleaned_data)
            
            #Enviar  e-mail de confirmação
            mail.send_mail('Confirmação de inscrição',
                           body,
                           'contato@eventex.com.br',
                           ['contato@eventex.com.br',form.cleaned_data['email']])
            
            messages.success(request,'Inscrição realizada com sucesso!!')
            
            return HttpResponseRedirect('/inscricao/')
         
        else:
            context = {'form' : form }
            response = render(request,'subscriptions/subscription_form.html', context) 
            return response
        
    else:
        context = {'form' : SubscriptionForm() }
        response = render(request,'subscriptions/subscription_form.html', context) 
        return response