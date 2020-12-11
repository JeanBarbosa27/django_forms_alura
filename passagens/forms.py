from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validations import *


class PassagemForm(forms.Form):
    origem = forms.CharField(label='Origem:', max_length=100)
    destino = forms.CharField(label='Destino:', max_length=100)
    data_ida = forms.DateField(label='Ida:', widget=DatePicker())
    data_volta = forms.DateField(label='Volta:', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Pesquisado em:', initial=datetime.today, disabled=True)
    classe_viagem = forms.ChoiceField(label='Classe de vôo:', choices=tipos_de_classe)
    informacoes = forms.CharField(label='Informações extras:', required=False, widget=forms.Textarea())
    email = forms.EmailField(label='Email:', max_length=150)

    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        lista_erros = {}

        campo_tem_numero('origem', origem, lista_erros)
        campo_tem_numero('destino', destino, lista_erros)
        origem_e_destino_iguais(origem, destino, lista_erros)

        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)

