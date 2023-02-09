from django.http import HttpResponse
from django.shortcuts import redirect, render
import datetime
from .models import Transacao
from .form import TransacaoFomulario


# Create your views here.

def home(request):
    data = {}
    data['transacao'] = ['T1', 'T2', 'T3']

    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    data['transacoes'] = Transacao.objects.all()

    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    #
    data = {}
    formulario = TransacaoFomulario(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        return redirect('url_listagem')

    data["formulario"] = formulario
    return render(request, "contas/formulario.html", data)


def update(request, pk):
    data = {}
    transacao = Transacao.objects.get(pk=pk)
    formulario = TransacaoFomulario(request.POST or None, instance=transacao)

    if formulario.is_valid():
        formulario.save()
        return redirect('url_listagem')

    data["formulario"] = formulario
    data['transacao'] = transacao
    return render(request, "contas/formulario.html", data)


def delete(request, pk):

    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')
