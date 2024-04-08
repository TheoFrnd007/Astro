from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def usuarios(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def registro(request):
    template = loader.get_template('registro.html')
    return HttpResponse(template.render())