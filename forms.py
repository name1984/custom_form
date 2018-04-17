from .models import ExtraInfo
from django.forms import ModelForm

class ExtraInfoForm(ModelForm):
    """
    The field on this form are derived from the ExtraInfo model in models.py
    """
    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields['cedula'].error_messages ={
            "required" : "ES NECESARIO INGRESAR SU CEDULA DE CIUDADANIA",
            "invalid" : "INGRESE UNA CEDULA VALIDA",
        }

        class Meta(object):
            model = ExtraInfo
            fields = ('cedula')
