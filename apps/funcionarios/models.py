from django.db import models
from django.db.models import Sum
from django.urls import reverse
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.IntegerField('Código do Usuário')
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    de_ferias = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    @property
    def total_horas_extra(self):
        total = self.registro_hora_extra_set.filter(
            utilizada=False).aggregate(
            Sum('horas'))['horas__sum']
        return total or 0

    def __str__(self):
        return self.nome
