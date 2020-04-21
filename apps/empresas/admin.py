from django.contrib import admin
from apps.empresas.models import Empresa
from gestao_rh.MultiDBModelAdmin import MultiDBModelAdmin


class EmpresaAdmin(MultiDBModelAdmin):
    MultiDBModelAdmin.using = 'antigo'

admin.site.register(Empresa, EmpresaAdmin)
