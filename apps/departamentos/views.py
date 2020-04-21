from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from apps.departamentos.models import Departamento
from apps.funcionarios.models import Funcionario


class DeparatamentosList(ListView):
    model = Departamento
    # paginate_by = 10

    def get_queryset(self):
        user_id = self.request.user.id
        empresa_logada = Funcionario.objects.get(user=user_id).empresa_id
        return Departamento.objects.filter(empresa=empresa_logada)

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()

        return super(DepartamentoCreate, self).form_valid(form)

class DeparatamentoEdit(UpdateView):
    model = Departamento
    fields = ['nome']

class DeparatamentoDelete(DeleteView):
    model = Departamento

    # reverse_lazy não deixa concatenar a url
    success_url = reverse_lazy('list_departamentos')

