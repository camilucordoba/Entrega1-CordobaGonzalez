from django import forms
from clothes.models import Clothes

# class Product_form(forms.Form):
#     name = forms.CharField(max_length=40)
#     price = forms.FloatField()
#     description = forms.CharField(max_length=200)
#     bar_code = forms.CharField(max_length=30)
#     active = forms.BooleanField(required=False)


class Product_form(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = '__all__'
