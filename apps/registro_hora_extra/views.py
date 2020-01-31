from django.shortcuts import render
from django.views.generic import ListView, UpdateView

from apps.registro_hora_extra.models import Registro_hora_extra


class HoraExtraList(ListView):
    model = Registro_hora_extra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Registro_hora_extra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = Registro_hora_extra
    fields = ['motivo', 'funcionario', 'horas']

