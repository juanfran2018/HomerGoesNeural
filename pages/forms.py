from django import forms
from .models import Homer


class HomerForm(forms.ModelForm):

    class Meta:
        model = Homer
        fields = ('homer_picture',)
