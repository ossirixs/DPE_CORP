#Django.
from django import forms
#Models.
from company.models import Company
from company.models import TestCode

class NewCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ('company_type','company_main','company_name','company_contact','company_phone','company_email')

    # def clean_company_main(self):
    #     """Company main (for branch companies) must be int"""
    #     company_main = self.cleaned_data['company_main']
    #     print('company main', company_main)
    #     if company_main.is_integer():
    #         return company_main
    #     else:
    #         raise forms.ValidationError('Company main not an integer')


class TestCodeForm(forms.ModelForm):

    class Meta:
        model = TestCode
        fields = ['user' ,'company' ,'test' ,'code' ,'activate' ,'expiration' ]

