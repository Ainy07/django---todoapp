from django import forms
from .models import Create
from django.forms import ModelForm

class CreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Add New Task'}
    ))
    class Meta:
        model = Create
        fields = '__all__'