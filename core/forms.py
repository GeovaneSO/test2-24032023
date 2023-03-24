from django import forms
from .models import Consumer

class UploadFileForm(forms.Form):
    file = forms.FileField()

class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = '__all__'

