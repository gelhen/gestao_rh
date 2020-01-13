from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.funcionarios.models import Funcionario


@login_required
def home(request):
    usuario = request.user
    data = dict(usuario=usuario)
    return render(request, 'core/index.html', data)
