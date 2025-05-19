from django import forms
class EnForms(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    phone=forms.IntegerField()