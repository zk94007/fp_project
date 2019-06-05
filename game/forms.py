# yourapp.forms.py
from django.forms import ModelForm, TextInput, Textarea, URLInput
from .models import Game

# Create the form class.
class GameForm(ModelForm):

    class Meta:
        model = Game
        fields = ['title', 'link', 'desc']
        widgets = {
            'title': TextInput(attrs={'class': 'review-input', 'placeholder': 'Game Title'}),
            'link': URLInput(attrs={'class': 'review-input', 'placeholder': 'Embed Link'}),
            'desc': Textarea(attrs={'class': 'review-textarea', 'placeholder': "Game's Description"}),
        }
        labels = {
            'title': '',
            'link': '',
            'desc': '',
        }
