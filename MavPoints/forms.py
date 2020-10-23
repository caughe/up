from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Customer
from django.utils.translation import ugettext, ugettext_lazy as _


class CustomerForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
                                widget=forms.PasswordInput,
                                help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = Customer
        fields = ('username', 'cust_email', 'cust_first_name', 'cust_last_name',
                  'address', 'city', 'state', 'zipcode', 'phone_number',
                  'cust_bill_card', 'cust_bill_expiry', 'cust_bill_code',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(CustomerForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


