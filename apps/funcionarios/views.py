from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from apps.funcionarios.models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario
    # paginate_by = 10

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    #não deixa concatenar a url
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = ''
        for func in funcionario.nome.split(' '):
            username = username + func
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()

        return super(FuncionarioCreate, self).form_valid(form)
