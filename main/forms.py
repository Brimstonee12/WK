from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    tekst = forms.CharField(max_length=185)

    class Meta:
        model = Comment
        fields = ('autor', 'tekst','post')
