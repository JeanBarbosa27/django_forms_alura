from django.views import View
from django.shortcuts import render, redirect
from passagens.forms import PassagemForm, PessoaForm


class RevisaoConsultaView(View):
    """Administra renderização da página minha consulta conforme método da requisição"""

    def get(self, request):
        """Quando a requisição tiver o método get, volta direto para a página inicial"""

        return redirect('index')

    def post(self, request):
        """Quando a requisição tiver o método post, exibe na página as informações preenchidas na página inicial"""

        form = PassagemForm(request.POST)
        pessoa_form = PessoaForm(request.POST)

        if form.is_valid():
            contexto = { 'form': form, 'pessoa_form': pessoa_form }
            return render(request, 'minha_consulta.html', contexto)
        else:
            contexto = { 'form': form, 'pessoa_form': pessoa_form }
            return render(request, 'index.html', contexto)
