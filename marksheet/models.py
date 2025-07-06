from django.db import models
from django.forms import ValidationError
from django.urls import reverse 
# from django.utils.text import slugify
from django.core.validators import  MaxLengthValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from .fields import CaseInsensitiveCharField

# Create your models here.

#CREATING CUSTOM USER MODEL

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, mobile_no, email, password = None):
        if not first_name:
            raise ValueError("Enter First Name")
        elif not last_name:
            raise ValueError("Enter Last Name")
        elif not username:
            raise ValueError("Enter Proper Username")
        elif not mobile_no:
            raise ValueError("Enter Proper Mobile No")
        elif not email:
            raise ValueError("Enter Proper Email Address")
        
        user = self.model (
            first_name = first_name,
            last_name= last_name,
            username = username,
            mobile_no = mobile_no,
            email = self.normalize_email(email),           
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, username, mobile_no, email, password = None):
        user = self.create_user(
            first_name = first_name,
            last_name= last_name,
            username = username,
            mobile_no = mobile_no,
            email = self.normalize_email(email),
            password = password,
         )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    class Meta:
        db_table = 't_users'
        verbose_name_plural = 'Users'

    first_name = models.CharField(max_length=50, error_messages="Enter First Name")
    last_name = models.CharField(max_length=50, error_messages="Enter Last Name")
    username = models.CharField(max_length=50, unique=True, error_messages="Enter User Name")
    mobile_no = models.CharField(max_length=12, unique=True, error_messages="Enter Mobile Number")
    email = models.EmailField(max_length=50, unique=True)
    password= models.CharField(max_length=150) 

    #required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    #=============================================

    USERNAME_FIELD = 'username' #email can also be the username field
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'mobile_no']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


#END OF CUSTOM USER MODEL
class StudentProfile(models.Model):
    class Meta:
        db_table = 't_studentsprofile'
        verbose_name_plural = 'STUDENTS PROFILE'

    students_name = models.CharField(max_length=100, null=False, blank=False, db_index=True)
    regn_no = models.CharField(max_length=20, null=True, blank=True)   
    roll_no = models.CharField(max_length=20, default=None, null=False, blank=False, db_index=True, unique=True)    
    mobile_no = models.CharField(max_length=10, blank=True, null=True, validators=[MaxLengthValidator(10,"Mobile Number cannot be more than 10 Digits")] )
    alternate_no = models.CharField(max_length=10, blank=True, null=True, validators=[MaxLengthValidator(10,"Mobile Number cannot be more than 10 Digits")] )
    email_address = models.EmailField(max_length=50, unique=True, default=None)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Marksheet(models.Model):
    class Meta:
        db_table = 't_marksheet'
        verbose_name_plural = 'MARKSHEETS'
        
    student_id = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, default=0)    
    exam_year =  models.CharField(max_length=20, null=True, blank=True)
    certificate_upload = models.FileField(upload_to="certificate")
    marksheet_upload = models.FileField(upload_to="marksheet")
    remarks = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Marks(models.Model):
    class Meta:
          db_table = 't_marks'
          verbose_name_plural = "MARKS"

    marksheet_id = models.ForeignKey(Marksheet, on_delete=models.CASCADE)
    code = models.CharField(max_length=30, null=True)
    subjects = models.CharField(max_length=100)
    credit_earned = models.CharField(max_length=20, null=True)
    grade_points = models.CharField(max_length=20, null=True)
    grade_obtained = models.CharField(max_length=20, null=True)
    total_credits_earned = models.CharField(max_length=30, null=True)
    sgpa = models.CharField(max_length=30, null=True)




class PaperNo(models.Model):
    class Meta:
        db_table = 't_paperno'
        verbose_name_plural = "PAPER NUMBER"
        
    heads = models.CharField(max_length=30, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        self.heads = self.heads.capitalize()

class PaperType(models.Model):
    class Meta:
        db_table = 't_papertype'
        verbose_name_plural = "PAPER TYPE"
        
    heads = models.CharField(max_length=30, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        self.heads = self.heads.capitalize()

class Status(models.Model):
    class Meta:
        db_table = 't_status'
        verbose_name_plural = "STATUS"
        
    heads = models.CharField(max_length=30, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        self.heads = self.heads.capitalize()

class Organization(models.Model):
    class Meta:
        db_table = 't_organizationsetup'
        verbose_name_plural = "ORGANIZATION SETUP"
    
    heads = models.CharField(max_length=100)
    address_1 =models.CharField(max_length=100, blank=True, null=True)
    address_2 =models.CharField(max_length=100, blank=True, null=True)
    address_3 =models.CharField(max_length=100, blank=True, null=True)
    email_address= models.EmailField(max_length=100, blank=True, null=True)
    mobile_no = models.CharField(max_length=50, blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Semester(models.Model):
    class Meta:
        db_table = 't_semester'
        verbose_name_plural = "SEMESTER SETUP"
    
    heads = models.CharField(max_length=50, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
            self.heads = self.heads.upper()  # Convert 'name' to uppercase
            super().save(*args, **kwargs)  # Call the original save method

    def __str__(self):
        return self.heads

class Subjects(models.Model):
    class Meta:
        db_table = 't_subjects'
        verbose_name_plural = "SUBJECTS"
    
    semester_id = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="semester_subjects")
    code = models.CharField(max_length=30, blank=True, null=True)
    heads = models.CharField(max_length=100, unique=True, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        self.code = self.code.capitalize()
        self.heads = self.heads.capitalize()

class Batch(models.Model):
    class Meta:
        db_table = 't_batch'
        verbose_name_plural = "BATCH SETUP"
    
    heads = models.CharField(max_length=50, unique=True, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# def get_absolute_url(self):
#     return reverse("book-detail", kwargs={"pk": self.pk})

# def save(self,  *args, **kwargs): #OVERRIDING SAVE METHOD
#     self.slug = slugify(self.title)
#     super().save(*args, **kwargs)