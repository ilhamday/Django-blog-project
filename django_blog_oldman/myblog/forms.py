from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    content =  forms.CharField(widget=forms.Textarea(attrs={
        # like attributes in html for Textarea tag
        'class': 'form-control',
        'id': 'usercomment',
        'placeholder': 'Type your comment',
        'rows': 3,
    }))

    class Meta:
        model = Comment
        fields = ('content',)