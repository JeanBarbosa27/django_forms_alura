from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .classe_viagem import tipos_de_classe


class PassagemForm(forms.Form):
    origem = forms.CharField(label='Origem:', max_length=100)
    destino = forms.CharField(label='Destino:', max_length=100)
    data_ida = forms.DateField(label='Ida:', widget=DatePicker())
    data_volta = forms.DateField(label='Volta:', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Pesquisado em:', initial=datetime.today, disabled=True)
    classe_viagem = forms.ChoiceField(label='Classe de vôo:', choices=tipos_de_classe)
    informacoes = forms.CharField(label='Informações extras:', required=False, widget=forms.Textarea())
    email = forms.EmailField(label='Email:', max_length=150)

    def clean_origem(self):
        origem = self.cleaned_data.get('origem')

        if any(char.isdigit() for char in origem):
            raise forms.ValidationError(
                'Origem inválida: Números não são permitidos!'
            )
        else:
            return origem
