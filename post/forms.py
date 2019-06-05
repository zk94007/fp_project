# yourapp.forms.py
from django.forms import ModelForm, TextInput, Textarea
from post.models import Post

# Create the form class.
class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'title': TextInput(attrs={'class': 'review-input', 'placeholder': 'Post Subject', 'required': 'required', 'data-value-missing':'required'}),
            'body': Textarea(attrs={'class': 'review-textarea', 'placeholder': "Post's Description"}),
        }
        labels = {
            'title': '',
            'body': '',
        }
