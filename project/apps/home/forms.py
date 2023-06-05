from django import forms

from . import models

class AutorForm(forms.ModelForm):
    class Meta:
        model = models.Autor
        fields = "__all__"
        
class PostForm(forms.ModelForm):
    class Meta:
        model = models.
        fields = "__all__"
        
        
        