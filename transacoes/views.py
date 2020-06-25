import os
import requests
from django.shortcuts import render


def index(request):
    return render(request, 'transacoes/index.html', {'user': None})


def login(request):
    return render(request, 'transacoes/login.html')


def contas(request):
    url_api = os.getenv('URL_API') + 'contas'
    response = requests.get(url_api)
    contas = response.json()
    return render(request, 'transacoes/contas.html', {'contas': contas})


def conta_v(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta
    url_transacoes_conta = os.getenv('URL_API') + 'transacoes/conta/' + idconta

    response_conta = requests.get(url_conta)
    response_transacoes_conta = requests.get(url_transacoes_conta)

    conta = response_conta.json()
    transacoes = response_transacoes_conta.json()
    return render(request, 'transacoes/conta_v.html', {'conta': conta, 'transacoes': transacoes})


def transacao_new(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta
    url_tp_transacoes = os.getenv('URL_API') + 'tipo-transacoes'

    response_conta = requests.get(url_conta)
    response_tp_transacoes = requests.get(url_tp_transacoes)

    conta = response_conta.json()
    tp_transacoes = response_tp_transacoes.json()
    return render(request, 'transacoes/transacao.html', {'conta': conta, 'tipo_transacoes': tp_transacoes})