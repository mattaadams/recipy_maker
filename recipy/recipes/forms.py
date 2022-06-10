from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body', 'recipe']

        widgets = {
            'recipe': forms.TextInput(attrs={'type': 'hidden'}),
        }
