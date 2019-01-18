import unicodedata

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory

from beers.models import Company, Beer

"""class CompanyForm(forms.Form):
    name = forms.CharField(required=True)
    tax_number = forms.IntegerField(required=True, label="CIF", initial=0)"""

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['created_at','created_by','last_modified_by','last_modified_at']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "company-form"
        self.helper.form_class = "blue"

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


class LoginPruebaForm(AuthenticationForm):
    username = forms.CharField(
        label='Usuario',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario'
            }
        )
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña'
            }
        )
    )

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.helper = FormHelper()
        self.helper.add_input(Submit('submit-button',"Iniciar Sesion"))
        self.helper.form_class = "form-signin"
        self.helper.label_class = "sr-helper"
        self.helper.form_method = "post"

class BeerForm(forms.ModelForm):
    class Meta:
        model = Beer
        exclude = ['created_at', 'created_by', 'last_modified_by', 'last_modified_at']


BeerFormset = inlineformset_factory(Company, Beer, form=BeerForm, extra=2)

