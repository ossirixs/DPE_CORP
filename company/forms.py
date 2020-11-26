#Django.
from django import forms
from django.contrib.auth import get_user_model

#Models.
from company.models import Company

class NewCompanyForm():
    first_name = forms.CharField(max_length=255)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Company
        fields = ('email','username', 'first_name', 'last_name','second_last_name','company', 'type')