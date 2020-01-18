from django.urls import path, include
from apps.funcionarios.views import FuncionariosList, FuncionarioEdit, FuncionarioDelete


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
