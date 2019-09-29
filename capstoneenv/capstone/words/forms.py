from django import forms
from .models import Word, Text


class WordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = (
            'word', 'isGood', 'created_by'
        )


class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = (
            'title', 'content', 'created_by'
        )