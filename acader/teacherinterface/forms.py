from django import forms
from .models import Profile1


class BioUpdate1(forms.ModelForm):
    class Meta:
        model = Profile1
        fields = ['description','image']


