from django.views.generic.list import ListView
from apps.funcionarios.models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario
    paginate_by = 10
