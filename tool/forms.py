# yourapp.forms.py
from django.forms import ModelForm, TextInput, Textarea, URLInput
from .models import Tool

# Create the form class.
class ToolForm(ModelForm):

    class Meta:
        model = Tool
        fields = ['title', 'link', 'desc']
        widgets = {
            'title': TextInput(attrs={'class': 'review-input', 'placeholder': 'Tool Title'}),
            'link': URLInput(attrs={'class': 'review-input', 'placeholder': 'Tool Link'}),
            'desc': Textarea(attrs={'class': 'review-textarea', 'placeholder': "Tool's Description"}),
        }
        labels = {
            'title': '',
            'link': '',
            'desc': '',
        }
