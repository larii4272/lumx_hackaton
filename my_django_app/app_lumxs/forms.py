from django import forms

from backend_lumx import project, contract, wallet

# Form to add new Pill to an Elder
class CreateContract(forms.Form):
    name = forms.CharField(max_length=100)
    symbol = forms.IntegerField(min_value=0)
    description = forms.CharField(max_length=100)
    type_ = forms.CharField(max_length=100)
    
    def __init__(self, user, *args, **kwargs):
        super(CreateContract, self).__init__(*args, **kwargs)
        self.user = user

    def save_contract(self):
        project = self.user.project
        my_contract = contract.Contract(project)
        # Obtendo os valores dos campos do formulário
        name = self.cleaned_data['name']
        symbol = self.cleaned_data['symbol']
        description = self.cleaned_data['description']
        type_ = self.cleaned_data['type_']
        # Passando os valores para o método create_contract
        my_contract.create_contract(name, symbol, description, type_)


