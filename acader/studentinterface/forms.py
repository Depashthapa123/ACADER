from django import forms
from .models import Profile


class BioUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description','image']


