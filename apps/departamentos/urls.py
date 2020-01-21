from django.urls import path, include
from .views import DeparatamentosList, DepartamentoCreate, DeparatamentoEdit, DeparatamentoDelete


urlpatterns = [
    path('list', DeparatamentosList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('editar/<int:pk>/', DeparatamentoEdit.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DeparatamentoDelete.as_view(), name='delete_departamento'),
]
