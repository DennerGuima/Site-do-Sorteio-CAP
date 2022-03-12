
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Clientes

# Create your views here.
from django.urls import reverse_lazy

#pagina cadastros --------C

class ClientesCad(CreateView):
    model = Clientes
    fields = ['cpf','dn', 'rua','numero', 'bairro', 'turma', 'nome_resp', 'sexo', 'telefone', 'email']
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

#pagina listagems --------R

class ClientesListagem(ListView):
    model = Clientes
    template_name = 'cadastros/listar_cadastros.html'

#pagina Editar --------U

class ClientesUpdate(UpdateView):
    model = Clientes
    fields = "__all__"
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

#pagina Deletar --------D


class ClientesDelete(DeleteView):
    model = Clientes
    template_name = 'cadastros/excluir_cadastros.html'
    success_url = reverse_lazy('listagem')

def abertura_modelform(request):
    return render(request, 'index.html')