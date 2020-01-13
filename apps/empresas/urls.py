from django.urls import path
from .views import EmpresaCreate


urlpatterns = [
    path('novo', EmpresaCreate.as_view(), name='empresa_create'),
]
