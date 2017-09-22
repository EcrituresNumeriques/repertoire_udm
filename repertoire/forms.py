from django.forms import ModelForm
from .models import Oeuvre

class ELementForm(ModelForm):
    class Meta:
        model = Oeuvre
        fields = [ 'titre', 'auteur', ]
