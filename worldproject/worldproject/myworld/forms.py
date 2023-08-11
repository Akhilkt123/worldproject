from django import forms
from . models import world


class WorldForm(forms.ModelForm):
    class Meta:
        model=world
        fields=['name','desc','year','img']