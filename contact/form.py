from django import forms
from . models import CustomerMessage

class CustomerMessageForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = [ 'name',
                  'email',
                  'phone',
                  'subject',
                  'message', 
                   ]

