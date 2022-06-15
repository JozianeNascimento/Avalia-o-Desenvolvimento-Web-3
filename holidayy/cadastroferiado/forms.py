from django.forms import ModelForm

from cadastroAPI.models import FeriadoModel


class FeriadoForm(ModelForm):
    class Meta:
        model = FeriadoModel
        fields = ['nome', 'data']