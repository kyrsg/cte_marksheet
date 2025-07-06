from django import forms
from .models import User, Subjects, Semester, Batch, Marksheet, StudentProfile

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
            self.fields['first_name'].widget.attrs['autocomplete'] = 'off'
            self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
            self.fields['last_name'].widget.attrs['autocomplete'] = 'off'
            self.fields['username'].widget.attrs['placeholder'] = 'Username'
            self.fields['username'].widget.attrs['autocomplete'] = 'off'
            self.fields['mobile_no'].widget.attrs['placeholder'] = 'Mobile No'
            self.fields['mobile_no'].widget.attrs['autocomplete'] = 'off'
            self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
            self.fields['email'].widget.attrs['autocomplete'] = 'off'
            self.fields['password'].widget.attrs['placeholder'] = 'Password'
            self.fields['confirm_password'].widget.attrs['placeholder'] = 'Confirm Password'          

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
       

        if password != confirm_password:
            raise forms.ValidationError("Password does not match !!")
        
        

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['semester_id', 'code', 'heads']

   
    semester_id = forms.ModelChoiceField(queryset=Semester.objects.all(), widget=forms.Select(attrs={'style': 'text-transform: uppercase;'}))
    code = forms.CharField(max_length=30)
    heads = forms.CharField(max_length=100)    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            self.fields['semester_id'].widget.attrs['placeholder'] = 'Select Semester'         
            self.fields['code'].widget.attrs['placeholder'] = 'Enter Code'
            self.fields['code'].widget.attrs['autocomplete'] = 'off'
            self.fields['heads'].widget.attrs['placeholder'] = 'Enter Subject Name'
            self.fields['heads'].widget.attrs['autocomplete'] = 'off'
          
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['heads', 'address_1', 'address_2', 'address_3', 'email_address', 'mobile_no']

    heads = forms.CharField(max_length=100)
    address_1 = forms.CharField(max_length=100)
    address_2 = forms.CharField(max_length=100)
    address_3 = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=50)
    mobile_no = forms.CharField(max_length=100)
    

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


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['heads']
   
    heads = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'style': 'text-transform: uppercase;'}))    

   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # self.fields['heads'].widget.attrs['placeholder'] = 'Enter Semester Name'
            self.fields['heads'].widget.attrs['autocomplete'] = 'off'

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['heads']
   
    heads = forms.CharField(max_length=50)    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            self.fields['heads'].widget.attrs['placeholder'] = 'Enter Batch Name' 
            self.fields['heads'].widget.attrs['autocomplete'] = 'off'

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
   
    username = forms.CharField(max_length=50) 
    password = forms.CharField(widget=forms.PasswordInput())   

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'Enter Username' 
            self.fields['password'].widget.attrs['placeholder'] = 'Enter Password'



class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['students_name', 'regn_no', 'roll_no', 'mobile_no', 'alternate_no', 'email_address']

    students_name = forms.CharField(max_length=100)
    regn_no = forms.CharField(max_length=100)
    roll_no = forms.CharField(max_length=100)
    mobile_no = forms.CharField(max_length=10, widget=forms.NumberInput())
    alternate_no = forms.CharField(max_length=10, widget=forms.NumberInput())
    email_address = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}))

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            self.fields['students_name'].widget.attrs['placeholder'] = 'Enter Students Name'
            self.fields['students_name'].widget.attrs['autocomplete'] = 'off'

            self.fields['regn_no'].widget.attrs['placeholder'] = 'Enter Registration Number'
            self.fields['regn_no'].widget.attrs['autocomplete'] = 'off'

            self.fields['roll_no'].widget.attrs['placeholder'] = 'Enter Roll No'
            self.fields['roll_no'].widget.attrs['autocomplete'] = 'off'

            self.fields['mobile_no'].widget.attrs['placeholder'] = 'Mobile No'
            self.fields['mobile_no'].widget.attrs['autocomplete'] = 'off'

            self.fields['alternate_no'].widget.attrs['placeholder'] = 'Alternate Mobile No'
            self.fields['alternate_no'].widget.attrs['autocomplete'] = 'off'
            
            self.fields['email_address'].widget.attrs['autocomplete'] = 'off'
          


# class MarksheetForm(forms.ModelForm):
#     class Meta:
#         model = Marksheet
#         fields = ['roll_no', 'regn_no', 'students_name', 'address_3', 'email_address', 'mobile_no']

#     heads = forms.CharField(max_length=100)
#     address_1 = forms.CharField(max_length=100)
#     address_2 = forms.CharField(max_length=100)
#     address_3 = forms.CharField(max_length=100)
#     email_address = forms.EmailField(max_length=50)
#     mobile_no = forms.CharField(max_length=100)
    

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.fields.values():
#             field.widget.attrs['class'] = 'form-control'
#             self.fields['heads'].widget.attrs['placeholder'] = 'Enter Organization Name'
#             self.fields['address_1'].widget.attrs['placeholder'] = 'Address 1'
#             self.fields['address_2'].widget.attrs['placeholder'] = 'Address 2'
#             self.fields['address_3'].widget.attrs['placeholder'] = 'Address 3'
#             self.fields['email_address'].widget.attrs['placeholder'] = 'Email Address'
#             self.fields['mobile_no'].widget.attrs['placeholder'] = 'Mobile No'
