from django.urls import path, include
from apps.funcionarios.views import home


urlpatterns = [
    path('', home),
]
