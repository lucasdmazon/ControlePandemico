from django.db import models
from app.models import Dado
from django import forms


class FormDado(forms.ModelForm):
    class Meta:
        model = Dado
        exclude = ()
