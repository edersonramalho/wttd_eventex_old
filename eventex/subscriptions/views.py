#from django.http.response import HttpResponse
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    context = {'form' : SubscriptionForm() }
    response = render(request,'subscriptions/subscription_form.html', context) 
    return response