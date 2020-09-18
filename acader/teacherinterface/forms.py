from django import forms
from .models import Profile1, postmessage
from django.views.generic.edit import CreateView


class BioUpdate1(forms.ModelForm):
    description = forms.CharField(
                        required=True, 
                        widget=forms.Textarea(
                                attrs={
                                    "placeholder": "Write about yourself, come on don't be shy!!",
                                    "class": "textinput",
                                }
                            )
                        )

    class Meta:
        model = Profile1
        fields = ['description', 'image']




