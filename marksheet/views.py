from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.views import View
from .forms import UserForm, OrganizationForm, SubjectForm, SemesterForm, BatchForm, LoginForm
from .models import User, Organization, Subjects, Semester, Batch
from django.contrib import messages, auth 
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
# Create your views here.

class IndexView(View):
   
    def get(self, request):
        context = {
            'active': 'active',
        }
        return render(request, "marksheet/index.html", context)

#===============LOGIN VIEW BEGINS HERE ==========================
class LoginView(View):
    def get(self, request):      
       
       if request.user.is_authenticated :
            return redirect('/')
       else:
            return render(request, "marksheet/login.html")

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request,user)
            messages.success(request, "User Login Successfull !!!")
            return redirect("/")
        else:
            messages.error(request, "Invalid Login Credentials !!!")
            return redirect('/login')
 #===============LOGIN VIEW ENDS HERE ==========================

 #===============LOGOUT VIEW BEGINS HERE ==========================
class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        messages.info(request, "You are logout successfully !!!")
        return render(request, "marksheet/login.html") 

 #===============LOGOUT VIEW ENDS HERE ==========================
     


 #===============ORGANIZATION VIEW BEGINS HERE ==========================
class OrganizationView(View):
   def get(self, request):
        get_id = Organization.objects.all()[0].id

        if get_id >0:
            organization = get_object_or_404(Organization, pk=get_id)
            form = OrganizationForm(instance=organization)          
        else:
            form = OrganizationForm()
        context = {
            'form' : form,         
            'organization_active': 'active',            
        }
        
        return render(request, "marksheet/organisation.html", context)
       
   def post(self,request):
        get_id = Organization.objects.all()[0].id

        if get_id >0:          
            pk = get_object_or_404(Organization, pk=get_id)
            form = OrganizationForm(request.POST,instance=pk) 
           
            # form.save(heads=heads, address_1=address_1, address_2=address_2, address_3=address_3, mobile_no=mobile_no, email_address=email_address)  
            form.save()
            messages.success(request, "Organization Updated Successfully !!!")             
            return redirect('/organization-setup')
           
        else:         
            form = OrganizationForm(request.POST)  

            if form.is_valid():               
                form.save()  
                messages.success(request, "Organization Configured Successfully !!!")  
                return redirect('/organization-setup') 
            else:            
                
                form = OrganizationForm(request.POST)
                context = {
                    'form' : form,         
                    'organization_active': 'active',                
                }               
                return render(request, "marksheet/organisation.html", context)        

 #===============ORGANIZATION VIEW ENDS HERE ==========================

#===============SUBJECT VIEW BEGINS HERE ==========================
class SubjectAddView(View):
    def get(self, request):
        form = SubjectForm()
        subject = Subjects.objects.all().order_by('code')
        context = {
            'form' : form,         
            'subjects_active': 'active',
            'table_name' : subject,
        }
        return render(request, "marksheet/subjects/add.html", context)

    def post(self, request):        
        form = SubjectForm(request.POST)
        subject = Subjects.objects.all().order_by('code')
        if form.is_valid():
            form.save()  
            messages.success(request, "Subjects Saved Successfully !!!")   
        else:
            form = SubjectForm(request.POST)
            context = {
                'form' : form,         
                'subjects_active': 'active',
                'table_name' : subject,
            }
            return render(request, "marksheet/subjects/add.html", context)
        return redirect('/subject/index')
       
    

class SubjectEditView(View):
    def get(self, request, pk=None):
     
        subject = get_object_or_404(Subjects, pk=pk)
        form = SubjectForm(instance=subject)          
        
        context = {
            'form' : form,         
            'subjects_active': 'active',
            'table_name' : subject,
        }
        
        return render(request, "marksheet/subjects/edit.html", context)

    def post(self, request, pk=None):
        
        subject = get_object_or_404(Subjects, pk=pk)
        form = SubjectForm(request.POST, instance=subject)     
      
        if form.is_valid():
            form.save()  
            messages.success(request, "Subjects Updated Successfully !!!")   
            
        else:
            form = SubjectForm(request.POST)
            context = {
                'form' : form,         
                'subjects_active': 'active',
                'table_name' : subject,
            }
            return render(request, "marksheet/subjects/edit.html", context)
            
       
        return redirect('/subject/index')


class SubjectDeleteView(View):
    def get(self, request, pk=None):
        subject = get_object_or_404(Subjects, pk=pk)
        subject.delete()
        messages.warning(request, "Subjects Deleted Successfully !!!")   
        return redirect('/subject/index')      
      
#==================SUBJECT VIEW ENDS HERE ==================================



#===================SEMESTER VIEW BEGINS HERE ==============================

class SemesterAddView(View):
   
    def get(self, request):
        form = SemesterForm()
        semester = Semester.objects.all().order_by('heads')
        
        context = {
            'form' : form,         
            'semester_active': 'active',
            'table_name' : semester,
        }
        return render(request, "marksheet/semester/add.html", context)

    def post(self, request):        
        form = SemesterForm(request.POST)
        semester = Semester.objects.all().order_by('heads')

       
        if form.is_valid():
            form.save()  
            messages.success(request, "Semester Saved Successfully !!!")   
        else:
            form = SemesterForm(request.POST)
            context = {
                'form' : form,         
                'semester_active': 'active',
                'table_name' : semester,
            }

            return render(request, "marksheet/semester/add.html", context)
        
        return redirect('/semester/index')

class SemesterEditView(View):
    def get(self, request, pk=None):
     
        semester = get_object_or_404(Semester, pk=pk)
        form = SemesterForm(instance=semester)          
        
        context = {
            'form' : form,         
            'semester_active': 'active',
            'table_name' : semester,
        }
        
        return render(request, "marksheet/semester/edit.html", context)

    def post(self, request, pk=None):
        
        semester = get_object_or_404(Semester, pk=pk)
        form = SemesterForm(request.POST, instance=semester)     
      
        if form.is_valid():
            form.save()  
            messages.success(request, "Semester Updated Successfully !!!")   
        else:
            context = {
                'form' : form,         
                'semester_active': 'active',
                'table_name' : semester,
            }
       
            return render(request, "marksheet/semester/edit.html", context)
        return redirect('/semester/index')


class SemesterDeleteView(View):
    def get(self, request, pk=None):
        semester = get_object_or_404(Semester, pk=pk)
        semester.delete()
        messages.warning(request, "Semester Deleted Successfully !!!")     
        return redirect('/semester/index')      
      
#==================SEMESTER VIEW ENDS HERE ==================================


#===================BATCH VIEW BEGINS HERE ==============================
class BatchAddView(View):
    def get(self, request):
        form = BatchForm()
        batch = Batch.objects.all().order_by('heads')
        
        context = {
            'form' : form,         
            'batch_active': 'active',
            'table_name' : batch,
        }
        return render(request, "marksheet/batch/add.html", context)

    def post(self, request):        
        form = BatchForm(request.POST)
        batch = Batch.objects.all().order_by('heads')

       
        if form.is_valid():
            form.save()  
            messages.success(request, "Batch Saved Successfully !!!")   
        else:
            form = BatchForm(request.POST)
            context = {
                'form' : form,         
                'batch_active': 'active',
                'table_name' : batch,
            }

            return render(request, "marksheet/batch/add.html", context)
        
        return redirect('/batch/index')

class BatchEditView(View):
    def get(self, request, pk=None):
     
        batch = get_object_or_404(Batch, pk=pk)
        form = SemesterForm(instance=batch)          
        
        context = {
            'form' : form,         
            'batch_active': 'active',
            'table_name' : batch,
        }
        
        return render(request, "marksheet/batch/edit.html", context)

    def post(self, request, pk=None):
        
        batch = get_object_or_404(Batch, pk=pk)
        form = BatchForm(request.POST, instance=batch)     
      
        if form.is_valid():
            form.save()  
            messages.success(request, "Batch Updated Successfully !!!")   
        else:
            context = {
                'form' : form,         
                'batch_active': 'active',
                'table_name' : batch,
            }
       
            return render(request, "marksheet/batch/edit.html", context)
        return redirect('/batch/index')


class BatchDeleteView(View):
    def get(self, request, pk=None):
        batch = get_object_or_404(Batch, pk=pk)
        batch.delete()
        messages.warning(request, "Batch Deleted Successfully !!!")   
        return redirect('/batch/index')      
      
#==================BATCH VIEW ENDS HERE ==================================

class RegisterView(View):
    def get(self, request):
        user = User.objects.all()
        form = UserForm()
        context = {
            'form' : form,
            'userdetail': user,
            'register_active': 'active',
        }
        return render(request, "marksheet/register.html", context)

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():   

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            mobile_no = form.cleaned_data['mobile_no']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']         

            try:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, mobile_no=mobile_no, email=email, password=password)
                user.save()
                
                    
                messages.success(request, "Your account has been registered successfully !!!")
                response = HttpResponseRedirect('/register')
                return response
            except:
                context = {
                'form' : form,
                'registeractive': 'active',
                }
            return render(request, "marksheet/register.html", context)
        else:
            context = {
                'form' : form,         
                'register_active': 'active',
                'table_name' : User,
            }
            return render(request, "marksheet/register.html", context)
        return redirect('/register')
             

#===================MARKSHEET VIEW BEGINS HERE ==============================
class MarksheetAddView(View):
    def get(self, request):
        form = BatchForm()
        batch = Batch.objects.all().order_by('heads')
        
        context = {
            'form' : form,         
            'batch_active': 'active',
            'table_name' : batch,
        }
        return render(request, "marksheet/batch/add.html", context)

    def post(self, request):        
        form = BatchForm(request.POST)
        batch = Batch.objects.all().order_by('heads')

       
        if form.is_valid():
            form.save()  
            messages.success(request, "Batch Saved Successfully !!!")   
        else:
            form = BatchForm(request.POST)
            context = {
                'form' : form,         
                'batch_active': 'active',
                'table_name' : batch,
            }

            return render(request, "marksheet/batch/add.html", context)
        
        return redirect('/batch/index')

class BatchEditView(View):
    def get(self, request, pk=None):
     
        batch = get_object_or_404(Batch, pk=pk)
        form = SemesterForm(instance=batch)          
        
        context = {
            'form' : form,         
            'batch_active': 'active',
            'table_name' : batch,
        }
        
        return render(request, "marksheet/batch/edit.html", context)

    def post(self, request, pk=None):
        
        batch = get_object_or_404(Batch, pk=pk)
        form = BatchForm(request.POST, instance=batch)     
      
        if form.is_valid():
            form.save()  
            messages.success(request, "Batch Updated Successfully !!!")   
        else:
            context = {
                'form' : form,         
                'batch_active': 'active',
                'table_name' : batch,
            }
       
            return render(request, "marksheet/batch/edit.html", context)
        return redirect('/batch/index')


class BatchDeleteView(View):
    def get(self, request, pk=None):
        batch = get_object_or_404(Batch, pk=pk)
        batch.delete()
        messages.warning(request, "Batch Deleted Successfully !!!")   
        return redirect('/batch/index')      
      
#==================BATCH VIEW ENDS HERE ==================================