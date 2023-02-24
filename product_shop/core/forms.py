from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['email', 'phone_num', 'cnt']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'order-form-input'}),
            'phone_num': forms.TextInput(attrs={'class':'order-form-input'}),
            'cnt': forms.TextInput(attrs={'class':'order-form-input'})    
        }
