from .models import dish
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class dishForm(forms.ModelForm):
    text = forms.CharField(widget=SummernoteWidget())
    
    class Meta:
        model = dish
        fields = ['name', 'text', 'featured_image']
       
