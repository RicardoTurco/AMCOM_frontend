"""amcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from transacoes.views import index, login, contas, conta_v, transacao_new, \
    confirm_transacao, delete_transacao, inativar_conta, ativar_conta, deletar_conta


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('contas/', contas, name='contas'),
    path('inativar-conta/<str:idconta>', inativar_conta, name='inativar_conta'),
    path('ativar-conta/<str:idconta>', ativar_conta, name='ativar_conta'),
    path('contas-v/<str:idconta>', conta_v, name='conta_v'),
    path('deletar-conta/<str:idconta>', deletar_conta, name='deletar_conta'),
    path('transacao-new/<str:idconta>', transacao_new, name='transacao_new'),
    path('confirm-transacao/', confirm_transacao, name='confirm_transacao'),
    path('delete-transacao/<str:idconta>/<str:idtransacao>', delete_transacao, name='delete_transacao'),
    path('admin/', admin.site.urls),
]
