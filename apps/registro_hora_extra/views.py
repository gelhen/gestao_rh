from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from apps.registro_hora_extra.models import Registro_hora_extra


class HoraExtraList(ListView):
    model = Registro_hora_extra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Registro_hora_extra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = Registro_hora_extra
    fields = ['motivo', 'funcionario', 'horas']


class HoraExtraDelete(DeleteView):
    model = Registro_hora_extra
    success_url = reverse_lazy('list_hora_extra')
