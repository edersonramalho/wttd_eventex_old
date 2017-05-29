from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from django.http.response import HttpResponseRedirect
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
#from django.template.context_processors import request
#from lib2to3.fixes.fix_input import context
from django.conf import settings

def subscribe(request):
    
    if (request.method == 'POST'):
        return create(request)
    else:
        return new(request)
        
"""
Função que cria a inscrição
"""
def create(request):
    # Pegar dados do Form, como String
    form = SubscriptionForm(request.POST) 
    
    """
    se o form não for valido, ele aborta o resto
    da função com o return
    """
    if not( form.is_valid() ):
        return render(request,'subscriptions/subscription_form.html',
                          {'form' : form }) 
    
    #Enviar email
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               form.cleaned_data['email'],
               'subscriptions/subscription_email.txt',
               form.cleaned_data)

    #feedback do email
    messages.success(request,'Inscrição realizada com sucesso!!')
    
    return HttpResponseRedirect('/inscricao/')

"""
Função que gera o form vazio
"""        
def new(request):    
    response = render(request,'subscriptions/subscription_form.html',
                      {'form' : SubscriptionForm() }) 
    return response

def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_,to])