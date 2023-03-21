from django import forms
from .models import Task


class FormTask(forms.ModelForm):
    tache =forms.CharField(max_length=150,widget=forms.TextInput(attrs={'placeholder':'Entrer votre tache','class':'form-control form-control-lg'}), required=False)
    
    class Meta:
        model = Task
        fields = [
            'tache'
        ]