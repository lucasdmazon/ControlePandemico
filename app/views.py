from django.shortcuts import render, get_object_or_404
from .models import Dado


def index(request):
    dados = Dado.objects.all()
    return render(request, 'dados/index.html', {
        'dados': dados
    })


def ver_aluno(request, dado_id):
    dado = get_object_or_404(Dado, id=dado_id)
    return render(request, 'dados/ver_aluno.html', {
        'dados': dado
    })