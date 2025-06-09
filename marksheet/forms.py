from django import forms
from .models import User

class UserForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'mobile_no', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['mobile_no'].widget.attrs['placeholder'] = 'Mobile No'
            self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
            self.fields['password'].widget.attrs['placeholder'] = 'Password'
            self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'          

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match !!")
    

class OrganizationForm(forms.Form):
    heads = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField()
    address_3 = forms.CharField()
    email_address = forms.EmailField()
    mobile_no = forms.CharField()
    website = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            self.fields['heads'].widget.attrs['placeholder'] = 'Enter Organization Name'
            self.fields['address_1'].widget.attrs['placeholder'] = 'Address 1'
            self.fields['address_2'].widget.attrs['placeholder'] = 'Address 2'
            self.fields['address_3'].widget.attrs['placeholder'] = 'Address 3'
            self.fields['email_address'].widget.attrs['placeholder'] = 'Email Address'
            self.fields['mobile_no'].widget.attrs['placeholder'] = 'Mobile No'
            self.fields['website'].widget.attrs['placeholder'] = 'Website'  
            