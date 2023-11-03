from django import forms
from django_countries.fields import CountryField

class CheckoutForm(forms.Form):
    street_address = forms.CharField()
    street_address_2 = forms.CharField(required=False)
    country = CountryField(blank_label='(select country)')
    postcode = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.BooleanField(widget=forms.RadioSelect())
