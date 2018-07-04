from django import forms
from .models import Notes

class NoteForm(forms.Form):
    body = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    due_date = forms.DateTimeField()
