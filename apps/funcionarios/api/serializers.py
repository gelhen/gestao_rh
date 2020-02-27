from rest_framework import serializers
from apps.funcionarios.models import Funcionario
from apps.registro_hora_extra.api.serializers import Registro_hora_extraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registro_hora_extra_set =  Registro_hora_extraSerializer(many=True)

    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'departamentos', 'empresa', 'user', 'total_horas_extra', 'registro_hora_extra_set']

