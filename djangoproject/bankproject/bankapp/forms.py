from django import forms
from .models import Customer, District, SubArea, Branch, AccountType, Material


class AdditionalInfoForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'district', 'branch', 'subarea', 'account_type', 'materials_provide')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['district'].widget.attrs['id'] = 'district'
        self.fields['subarea'].widget.attrs['id'] = 'subarea'
        self.fields['branch'].widget.attrs['id'] = 'branch'
        self.fields['district'].queryset = District.objects.all()
        # self.fields['subarea'].queryset = SubArea.objects.none()
        # self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['subarea'].queryset = SubArea.objects.filter(district_id=district_id)
            except (ValueError, TypeError):
                pass

        if 'subarea' in self.data:
            try:
                subarea_id = int(self.data.get('subarea'))
                self.fields['branch'].queryset = Branch.objects.filter(subarea_id=subarea_id)
            except (ValueError, TypeError):
                pass

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class WikipediaForm(forms.Form):
    district = forms.ModelChoiceField(queryset=District.objects.all())


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'dob', 'age', 'gender', 'phone_number', 'mail_id', 'address', 'district', 'branch', 'subarea', 'account_type', 'materials_provide')
        widgets = {
            'materials_provide': forms.CheckboxSelectMultiple,
        }
