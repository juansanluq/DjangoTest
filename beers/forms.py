from django import forms
from django.core.exceptions import ValidationError

from beers.models import Company

"""class CompanyForm(forms.Form):
    name = forms.CharField(required=True)
    tax_number = forms.IntegerField(required=True, label="CIF", initial=0)"""

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['created_at','created_by','last_modified_by','last_modified_at']

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == "juan":
            raise ValidationError("No puedes utilizar este nombre", code="invalid")

        return name

    def clean_tax_number(self):
        tax = self.cleaned_data['tax_number']
        if tax == 0:
            raise ValidationError("El tax number no puede ser 0", code="invalid")

        return tax

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        tax_numer = self.cleaned_data.get('tax_number')

        if name == "pepe" and tax_numer < 3:
            self.add_error('tax_number',"No puede ser menor que 3")