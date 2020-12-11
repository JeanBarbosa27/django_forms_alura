from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from passagens.classe_viagem import tipos_de_classe
from passagens.validations import *
from passagens.models import Passagem, ClasseViagem, Pessoa


class PassagemForm(forms.ModelForm):
    data_pesquisa = forms.DateField(label='Pesquisado em:', initial=datetime.today, disabled=True)
    class Meta:
        model = Passagem
        fields = '__all__'
        labels = {
            'data_ida': 'Data de ida',
            'data_volta': 'Data de volta',
            'classe_viagem': 'Classe do vôo',
            'informacoes': 'Informações extras',
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }

    def clean(self):
        lista_erros = {}

        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')

        campo_tem_numero('origem', origem, lista_erros)
        campo_tem_numero('destino', destino, lista_erros)
        origem_e_destino_iguais(origem, destino, lista_erros)
        data_ida_anterior(data_ida, data_pesquisa, lista_erros)
        data_volta_anterior(data_ida, data_volta, lista_erros)

        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)


class PessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        exclude = ['nome']
