from django.forms import ModelForm
from .models import Registro_hora_extra
from apps.funcionarios.models import Funcionario


class Registro_hora_extraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        #user vem da funcao get_form_kwargs da class HoraExtraCreate
        super(Registro_hora_extraForm, self).__init__(*args, **kwargs)
        # a linha abaixo subscreve o funcionario do fields na class Meta
        user_id = user.id
        empresa_logada = Funcionario.objects.get(user=user_id).empresa_id

        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=empresa_logada)

    class Meta:
        model = Registro_hora_extra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']
