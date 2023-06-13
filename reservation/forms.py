from .models import dish
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class dishForm(forms.ModelForm):
    class Meta:
        model = dish
        fields = ('text')
        widgets = {
            'foo': SummernoteWidget(),
            'bar': SummernoteInplaceWidget(),
        }

