from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Dado
from django.core.paginator import Paginator


def index(request):
    dados = Dado.objects.order_by('-nome').filter(
        mostrar = True
    )
    paginator = Paginator(dados, 10)
    page = request.GET.get('page')
    dados = paginator.get_page(page)
    return render(request, 'dados/index.html', {
        'dados': dados
    })


def ver_aluno(request, dado_id):
    dado = get_object_or_404(Dado, id=dado_id)

    if not dado.mostrar:
        raise Http404()

    return render(request, 'dados/ver_aluno.html', {
        'dados': dado
    })