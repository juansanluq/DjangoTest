from django import forms

from beers.models import Company

"""class CompanyForm(forms.Form):
    name = forms.CharField(required=True)
    tax_number = forms.IntegerField(required=True, label="CIF", initial=0)"""

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['created_at','created_by','last_modified_by','last_modified_at']