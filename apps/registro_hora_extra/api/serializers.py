from rest_framework import serializers
from apps.registro_hora_extra.models import Registro_hora_extra


class Registro_hora_extraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro_hora_extra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']

