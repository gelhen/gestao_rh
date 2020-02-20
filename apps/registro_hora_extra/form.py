from django.forms import ModelForm
from .models import Registro_hora_extra
from apps.funcionarios.models import Funcionario


class Registro_hora_extraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        #user vem da funcao get_form_kwargs da class HoraExtraCreate
        super(Registro_hora_extraForm, self).__init__(*args, **kwargs)
        # a linha abaixo subscreve o funcionario do fields na class Meta
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = Registro_hora_extra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']
