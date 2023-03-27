from django import forms
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime

class ContactForm(forms.Form):
    email=forms.EmailField()
    date=forms.DateField(widget=AdminDateWidget())
    time=forms.DateField(widget=AdminTimeWidget())
    content=forms.CharField(widget=forms.Textarea)