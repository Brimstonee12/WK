from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    tekst = forms.CharField(max_length=185, widget=forms.Textarea(
    attrs={"rows":5,"cols":48}))

    class Meta:
        model = Comment
        fields = ('autor', 'tekst','post')
