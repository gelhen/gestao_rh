from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, TemplateView
from django.views.generic.list import ListView
from apps.funcionarios.models import Funcionario
import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.views import View

class FuncionariosList(ListView):
    model = Funcionario
    # paginate_by = 10

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    #reverse_lazy não deixa concatenar a url
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = ''
        for func in funcionario.nome.split(' '):
            username = username + func
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()

        return super(FuncionarioCreate, self).form_valid(form)

def relatorio_funcionarios(request):
    # Create a file-like buffer to receive PDF data.
    response = HttpResponse(content_type='application/pdf')
    #Content-Disposition serve para baixar o arquivo no pc quando clicado
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = io.BytesIO()
    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    #escrever no relatorio usando coordenadas x, y
    p.drawString(200, 810, "Relatório de Funcionários.")
    p.drawString(0, 800, "_" * 200)

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)
    str = 'Nome: %s  | Hora Extra: %f'
    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str%(funcionario.nome, funcionario.total_horas_extra))
        y -= 20
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response


class Render:

    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode('UTF-8')), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' %filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')


class PdfDebug(TemplateView):
    template_name = 'funcionarios/relatorio.html'
