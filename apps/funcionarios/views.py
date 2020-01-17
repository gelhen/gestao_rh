from django.views.generic.list import ListView
from apps.funcionarios.models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario
    # paginate_by = 10

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)
