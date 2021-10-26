from django.shortcuts import render
from .models import Dado


def index(request):
    dados = Dado.objects.all()
    return render(request, 'dados/index.html', {
        'dados': dados
    })