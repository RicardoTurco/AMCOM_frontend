import os
import requests
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'transacoes/index.html', {'user': None})


def login(request):
    return render(request, 'transacoes/login.html')


def contas(request):
    url_api = os.getenv('URL_API') + 'contas'
    response = requests.get(url_api)
    contas = response.json()
    return render(request, 'transacoes/contas.html', {'contas': contas, 'status_contas': response.status_code})


def inativar_conta(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta + '/inactivate'

    response = requests.put(url_conta)
    return redirect('conta_v', idconta)


def ativar_conta(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta + '/activate'

    response = requests.put(url_conta)
    return redirect('conta_v', idconta)


def conta_v(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta
    url_transacoes_conta = os.getenv('URL_API') + 'transacoes/conta/' + idconta

    response_conta = requests.get(url_conta)
    response_transacoes_conta = requests.get(url_transacoes_conta)

    conta = response_conta.json()
    transacoes = response_transacoes_conta.json()
    return render(request, 'transacoes/conta_v.html', {'conta': conta, 'transacoes': transacoes, 'status_transacoes': response_transacoes_conta.status_code})


def deletar_conta(request, idconta=None):
    url_transacoes_conta = os.getenv('URL_API') + 'transacoes/conta/' + idconta
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta

    response_transacoes = requests.delete(url_transacoes_conta)
    response_conta = requests.delete(url_conta)
    return redirect('contas')


def transacao_new(request, idconta=None):
    url_conta = os.getenv('URL_API') + 'contas/id/' + idconta
    url_tp_transacoes = os.getenv('URL_API') + 'tipo-transacoes'

    response_conta = requests.get(url_conta)
    response_tp_transacoes = requests.get(url_tp_transacoes)

    conta = response_conta.json()
    tp_transacoes = response_tp_transacoes.json()
    return render(request, 'transacoes/transacao.html', {'conta': conta, 'tipo_transacoes': tp_transacoes})


def confirm_transacao(request):
    url_transacao = os.getenv('URL_API') + 'transacoes'

    transacao = {
        'idconta': request.POST.get('idconta'),
        'idtipotransacao': request.POST.get('idtipotransacao'),
        'valor': float(request.POST.get('valor'))
    }
    response = requests.post(url_transacao, json=transacao)
    return redirect('conta_v', request.POST.get('idconta'))


def delete_transacao(request, idconta=None, idtransacao=None):
    url_transacao = os.getenv('URL_API') + 'transacoes/id/' + idtransacao

    response = requests.delete(url_transacao)
    return redirect('conta_v', idconta)
