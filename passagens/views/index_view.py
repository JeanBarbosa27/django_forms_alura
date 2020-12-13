from django.views import View
from django.shortcuts import render, redirect
from passagens.forms import PassagemForm, PessoaForm


class IndexView(View):
    """Administra renderização da página inicial conforme método da requisição"""

    def get(self, request):
        form = PassagemForm()
        pessoa_form = PessoaForm()

        contexto = { 'form': form, 'pessoa_form': pessoa_form }

        return render(request, 'index.html', contexto)



