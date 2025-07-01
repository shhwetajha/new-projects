from django import forms
from .models import *

class PartyForm(forms.ModelForm):
    class Meta:
        model=party
        fields=['party_name',"party_address"]
        widgets={
            'party_name':forms.TextInput(attrs={'class':'form-control form-control-sm','required':'true'}),
            'party_address':forms.TextInput(atts={'class':'form-control,form-control-sm','readonly':'true'})

        }
  
class PartyForm(forms.ModelForm):
    class Meta:
        model=party
        fields=['party_name','party_address']
        widgets={
            'party_name':forms.TextInput(attrs={'class':'form-control form-control-sm','required':True}),
            'party_address':forms.TextInput(attrs={'class':'form-control form-control-sm','required':True}),
            'party_date':forms.DateInput(attrs={'type':'date' ,'class':'form-control form-control-sm'},format="%Y-%m-%d"),
            # 'party_date':forms.DateInput(attrs={'type':'date','class':'form-control form-control-sm'},format="%Y-%m-%d"),
        }
    