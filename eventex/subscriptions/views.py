from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings

from eventex.subscriptions.forms import SubscriptionForm

from eventex.subscriptions.models import Subscription
from django.template.context_processors import request

def subscribe(request):
    
    if (request.method == 'POST'):
        return create(request)
    else:
        return new(request)
        

#Função que cria a inscrição
def create(request):
    # Pegar dados do Form, como String
    form = SubscriptionForm(request.POST) 
    
    
    #se o form não for valido, ele aborta o resto
    #da função com o return    
    if not( form.is_valid() ):
        return render(request,'subscriptions/subscription_form.html',
                          {'form' : form }) 
        
    subscription = Subscription.objects.create(**form.cleaned_data)
    
    #Enviar email
    _send_mail('Confirmação de inscrição',
               settings.DEFAULT_FROM_EMAIL,
               subscription.email,
               'subscriptions/subscription_email.txt',
               {'subscription': subscription})

    #feedback do email
    messages.success(request,'Inscrição realizada com sucesso!!')
    
    return HttpResponseRedirect('/inscricao/{}/'.format(subscription.pk))

#Função que gera o form vazio        
def new(request):    
    response = render(request,'subscriptions/subscription_form.html',
                      {'form' : SubscriptionForm() }) 
    return response

def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist: #Exception que todos os models 
        raise http404 
    
    '''subscription = Subscription(
        name='Ederson da Silva Santos',
        email='edersonramalho@gmail.com',
        cpf='12345678901',
        phone='27-998310978')'''
    return render(request,'subscriptions/subscription_detail.html', 
                  {'subscription': subscription})
    
def _send_mail(subject, from_, to, template_name, context):
    body = render_to_string(template_name, context)
    mail.send_mail(subject, body, from_, [from_,to])