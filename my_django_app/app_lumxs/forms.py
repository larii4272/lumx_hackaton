from django import forms

# Form to add new Pill to an Elder
class CreateContract(forms.Form):
    name = forms.CharField(max_length=100)
    symbol = forms.IntegerField(min_value=0)
    description = forms.CharField(max_length=100)
    type_ = forms.CharField(max_length=100)