from django import forms

class FromResisters(forms.Form):
    enter_fast_name = forms.CharField(max_length=30)
    last_name = forms.CharField()
    email = forms.EmailField(label_suffix=' -')
    batch = forms.CharField()

