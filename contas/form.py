from django.forms import ModelForm
from .models import Transacao


class TransacaoFomulario(ModelForm):
    class Meta:
        model = Transacao
        fields = ['descricao','valor','categor','data','observacao']