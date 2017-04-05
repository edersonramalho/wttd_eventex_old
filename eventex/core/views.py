from django.shortcuts import render
from django.template.context_processors import request


def home(request):
    return render(request,'index.html')
