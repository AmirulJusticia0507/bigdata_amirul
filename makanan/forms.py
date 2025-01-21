from django import forms
from .models import Makanan

class MakananForm(forms.ModelForm):
    class Meta:
        model = Makanan
        fields = '__all__'
