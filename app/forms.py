from django.forms import ModelForm
from app.models import Dado


class DadoForm(ModelForm):
    class Meta:
        model = Dado
        fields =['nome', 'sobrenome', 'telefone', 'email', 'data_criacao', 'numero', 'serie', 'data_nascimento', 'categoria', 'mostrar']