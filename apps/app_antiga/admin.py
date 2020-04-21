from django.contrib import admin
from .models import Teste


class TesteAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

admin.site.register(Teste, TesteAdmin)
