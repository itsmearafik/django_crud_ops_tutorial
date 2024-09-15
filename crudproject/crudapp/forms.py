from django import forms 
from .models import Orders 

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

        labels = {
            'oid':'Order ID',
            'fname': 'First Name',
            'lname': 'Last Name',
            'price': 'Price',
            'mail': 'Email ID',
            'addr': 'Address',
        }

        widgets = {
            'oid': forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
            'fname': forms.TextInput(attrs={'placeholder': 'eg. John'}),
            'lname': forms.TextInput(attrs={'placeholder': 'eg Doe'}),
            'price': forms.NumberInput(attrs={'placeholder': {'eg $ 100.00'}}),
            'mail': forms.EmailInput(attrs={'placeholder': 'eg. myemail@email.com'}),
            'addr': forms.Textarea(attrs={'placeholder': 'eg. USA'}),
        }