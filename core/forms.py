from django import forms

from .models import Consumer, DiscountRules


class UploadFileForm(forms.Form):
    file = forms.FileField()


class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = [
            "name",
            "document",
            "zip_code",
            "city",
            "state",
            "consumption",
            # "distributor_tax",
            "consumer_type",
        ]


class RulesForm(forms.ModelForm):
    class Meta:
        model = DiscountRules
        fields = "__all__"
        
