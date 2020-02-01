from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.registro_hora_extra.form import Registro_hora_extraForm
from apps.registro_hora_extra.models import Registro_hora_extra


class HoraExtraList(ListView):
    model = Registro_hora_extra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Registro_hora_extra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = Registro_hora_extra
    #fields = ['motivo', 'funcionario', 'horas'] # para filtrar a empresa foi criada a classe abaixo e comentado esta linha
    form_class = Registro_hora_extraForm

    def get_form_kwargs(self):
        #get_form_kwargs possui todos os argumento que serão passados par ao forms,
        #1 recupera a lista de argumento que serão passados para o forms
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        #2 injeto o user no kwargs,
        kwargs.update({'user':  self.request.user})
        return kwargs



class HoraExtraDelete(DeleteView):
    model = Registro_hora_extra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = Registro_hora_extra
    #fields = ['motivo', 'funcionario', 'horas'] # para filtrar a empresa foi criada a classe abaixo e comentado esta linha
    form_class = Registro_hora_extraForm

    def get_form_kwargs(self):
        #get_form_kwargs possui todos os argumento que serão passados par ao forms,
        #1 recupera a lista de argumento que serão passados para o forms
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        #2 injeto o user no kwargs,
        kwargs.update({'user':  self.request.user})
        return kwargs

