from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Dado
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


def index(request):
    dados = Dado.objects.order_by('-nome').filter(
        mostrar=True
    )
    paginator = Paginator(dados, 8)
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


def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        messages.add_message(request, messages.ERROR, 'Campo termo não pode ficar vazio.')
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')

    dados = Dado.objects.order_by('-nome').annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(numero__icontains=termo) | Q(serie__icontains=termo) | Q(categoria__nome__icontains=termo)
    )

    paginator = Paginator(dados, 10)
    page = request.GET.get('page')
    dados = paginator.get_page(page)
    return render(request, 'dados/busca.html', {
        'dados': dados
    })