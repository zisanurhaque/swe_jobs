from django import forms

class FilterForm(forms.Form):
    search = forms.CharField(required=False, label='search')
    company = forms.CharField(required=False, label='company')
    published_time = forms.CharField(required=False, label='published_time')
    salary = forms.CharField(required=False, label='salary')