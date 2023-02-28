from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная снтраница')
    
def group_posts(request):
    return HttpResponse('Группы')

# Create your views here.
