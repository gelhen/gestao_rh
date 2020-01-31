from django.urls import path, include
from apps.registro_hora_extra.views import HoraExtraList, HoraExtraEdit, HoraExtraDelete


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    # path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('editar/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
]
