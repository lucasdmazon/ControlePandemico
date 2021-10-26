from django.shortcuts import render
from .models import Dado


def index(request):
    dados = Dado.objects.all()
    return render(request, 'dados/index.html', {
        'dados': dados
    })


def ver_aluno(request, dado_id):
    dado = Dado.objects.get(id=dado_id)
    return render(request, 'dados/ver_aluno.html', {
        'dados': dado
    })