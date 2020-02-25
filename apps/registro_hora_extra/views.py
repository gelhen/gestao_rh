import csv
import json

import xlwt
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from apps.registro_hora_extra.form import Registro_hora_extraForm
from apps.registro_hora_extra.models import Registro_hora_extra


class HoraExtraList(ListView):
    model = Registro_hora_extra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Registro_hora_extra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = Registro_hora_extra
    #fields = ['motivo', 'funcionario', 'horas'] # para filtrar a empresa foi criada a classe abaixo e comentado esta linha
    form_class = Registro_hora_extraForm

    def get_form_kwargs(self):
        #get_form_kwargs possui todos os argumento que serão passados par ao forms,
        #1 recupera a lista de argumento que serão passados para o forms
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        #2 injeto o user no kwargs,
        kwargs.update({'user':  self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = Registro_hora_extra
    #fields = ['motivo', 'funcionario', 'horas'] # para filtrar a empresa foi criada a classe abaixo e comentado esta linha
    form_class = Registro_hora_extraForm

    # success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user':  self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = Registro_hora_extra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = Registro_hora_extra
    #fields = ['motivo', 'funcionario', 'horas'] # para filtrar a empresa foi criada a classe abaixo e comentado esta linha
    form_class = Registro_hora_extraForm

    def get_form_kwargs(self):
        #get_form_kwargs possui todos os argumento que serão passados par ao forms,
        #1 recupera a lista de argumento que serão passados para o forms
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        #2 injeto o user no kwargs,
        kwargs.update({'user':  self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        utilizada = self.request.POST['utilizada']
        registro_hora_extra = Registro_hora_extra.objects.get(id=kwargs['pk'])
        registro_hora_extra.utilizada = utilizada
        registro_hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps({
            'mensagem': 'Requisição executada',
            'horas': float(empregado.total_horas_extra),
            'utilizada': registro_hora_extra.utilizada
        })

        return HttpResponse(response, content_type='application/json')


class ExportarParaCSV(View):
    def get(self, resquest):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        registro_he = Registro_hora_extra.objects.filter(utilizada=False)


        writer = csv.writer(response)
        writer.writerow(['id', 'motivo', 'funcionario', 'Horas Restantes',
                         'Horas'])

        for reg in registro_he:
            writer.writerow([reg.id, reg.motivo, reg.funcionario,
                             reg.funcionario.total_horas_extra, reg.horas])

        return response


class ExportarParaExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="users.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['id', 'motivo', 'funcionario', 'Horas Restantes', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = Registro_hora_extra.objects.filter(utilizada=False)

        row_num = 1

        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.motivo, font_style)
            ws.write(row_num, 2, registro.funcionario.nome, font_style)
            ws.write(row_num, 3, registro.funcionario.total_horas_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num +=1
        wb.save(response)
        return response