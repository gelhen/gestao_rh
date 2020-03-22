from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from apps.funcionarios.models import Funcionario
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.core.serializers import UserSerializer, GroupSerializer
from .tasks import send_relatorio

@login_required
def home(request):
    usuario = request.user
    data = dict(usuario=usuario)
    return render(request, 'core/index.html', data)


def celery(request):
    send_relatorio.delay()
    return HttpResponse('Tarefa incluída na fila para execução')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

