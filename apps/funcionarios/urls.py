from django.urls import path, include
from apps.funcionarios.views import FuncionariosList


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
]
