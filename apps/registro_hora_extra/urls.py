from django.urls import path, include
from apps.registro_hora_extra.views import (
    HoraExtraList,
    HoraExtraEdit,
    HoraExtraEditBase,
    HoraExtraDelete,
    HoraExtraCreate
)


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('editar/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
]
