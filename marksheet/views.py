
# ============ DJANGO SHORTCUTS ============
from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse, get_object_or_404

# ============ DJANGO FORMS============
from .forms import UserForm, OrganizationForm, SubjectForm, SemesterForm, BatchForm, LoginForm, StudentProfileForm

# ============ DJANGO MODELS============
from .models import User, Organization, Subjects, Semester, Batch, StudentProfile

# ============ DJANGO VIEWS============
from django.views import View
from django.views.generic import TemplateView

# ============ DJANGO CONTRIB ============
from django.contrib import messages, auth 

# ============ DJANGO URLS============
from django.urls import reverse

# ============ DJANGO JSON HTTP============
from django.http import JsonResponse

# ============ DJANGO DB ERRORS============
from django.db import IntegrityError
# Create your views here.

def get_filtered_data(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request       
        
        selected_value = request.GET.get('selected_value')
             
        # Filter your data based on selected_value
        filtered_data = Subjects.objects.filter(semester_id=selected_value).values() # .values() returns a list of dictionaries

       
        return JsonResponse(list(filtered_data), safe=False)
    return JsonResponse({'error': 'Invalid request'}, status=400)


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
        # subject = Subjects.objects.select_related('semester_id')
        context = {
            'form' : form,         
            'subjects_active': 'active',
            'table_name' : subject,
        }
        return render(request, "marksheet/subjects/add.html", context)

    def post(self, request):        
           
           if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request 
              
                
                semester_id = request.POST.get('semester_id')
                my_instance = Semester.objects.get(pk=semester_id)             

                code = request.POST.get('code')
                heads = request.POST.get('heads')

                try:
                    instance = Subjects(semester_id = my_instance, code = code, heads = heads)
                    instance.save()
                    filtered_data = Subjects.objects.filter(semester_id=semester_id).values() # .values() returns a list of dictionaries
                   
                    return JsonResponse(list(filtered_data), safe=False)
                except:
                  
                    return JsonResponse({'status': 'Error Information', 'errors': "Subject with the Code : " + code + " Already Exist !!! "}, status=400)

               
                
              
               
                    # messages.error(request, "Duplicate Entry Found")
                    # return JsonResponse({'status': 'error', 'errors': "Duplicate Entry"}, status=400)

               
           
               
           else:
              form = SubjectForm(request.POST)                
              return JsonResponse({'status': 'error', 'errors': "Duplicate Entry"}, status=400)
           return JsonResponse({'error': 'Invalid request'}, status=400)
           



          

        #     print("ajax")
        #     form = SubjectForm(request.POST)
        #     subject = Subjects.objects.all().order_by('code')
        #     if form.is_valid():

        #         instance = form.save()
             
        #         success = "Created"
                
        #         # return JsonResponse({'status': 'success', 'id': instance.id, 'name': instance.heads}, safe=False) # Example data
        #         return HttpResponse(success)
        #         messages.success(request, "Subjects Saved Successfully !!!")

        #     else:
        #         form = SubjectForm(request.POST)
        #         context = {
        #             'form' : form,         
        #             'subjects_active': 'active',
        #             'table_name' : subject,
        #         }
        #         return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
        #     return JsonResponse({'error': 'Invalid request'}, status=400)
        #     #     # return render(request, "marksheet/subjects/add.html", context)
        #     # # return redirect('/subject/index')
       
    

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
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request
            subject = get_object_or_404(Subjects, pk=pk) 
            subject.delete()          
            return JsonResponse({'status': 'success', 'id': pk})            
        return JsonResponse({'status': 'error'})   
      
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
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request 
            try:
                heads = request.POST.get("heads")
              
                instance = Semester(heads=heads)                
                instance.save()
                return JsonResponse({'status': 'success', 'id' : instance.id, 'heads': instance.heads})
            except :
                return JsonResponse({'status': 'error',  'message' : 'Semester Already Exist'})
        return JsonResponse({'status' : 'Not a Valid AJAX Request'})
            

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
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request 
            try:
                heads = request.POST.get("heads")    
                instance = get_object_or_404(Semester, pk=pk)
                instance.heads =  heads
                instance.save() 
               
                return JsonResponse({'status': 'success', 'id' : instance.id, 'heads': instance.heads, 'redirect_url': reverse("semester-add")})
            except :
                return JsonResponse({'status': 'error',  'message' : 'Semester Already Exist'})
        return JsonResponse({'status' : 'Not a Valid AJAX Request'})
            


class SemesterDeleteView(View):
    def get(self, request, pk=None):
        semester = get_object_or_404(Semester, pk=pk)
        semester.delete()       
        return JsonResponse({'status':'success', 'id':pk, 'module': 'Semester'})      
      
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
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request 
            try:
                heads = request.POST.get("heads")
              
                instance = Batch(heads=heads)                
                instance.save()
                return JsonResponse({'status': 'success', 'id' : instance.id, 'heads': instance.heads})
            except :
                return JsonResponse({'status': 'error',  'message' : 'Batch Already Exist'})
        return JsonResponse({'status' : 'Not a Valid AJAX Request'})
            

class BatchEditView(View):
    def get(self, request, pk=None):
     
        batch = get_object_or_404(Batch, pk=pk)
        form = BatchForm(instance=batch)          
        
        context = {
            'form' : form,         
            'batch_active': 'active',
            'table_name' : batch,
        }
        
        return render(request, "marksheet/batch/edit.html", context)

    def post(self, request, pk=None):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request 
            try:
                heads = request.POST.get("heads")    
                instance = get_object_or_404(Batch, pk=pk)
                instance.heads =  heads
                instance.save() 
               
                return JsonResponse({'status': 'success', 'id' : instance.id, 'heads': instance.heads, 'redirect_url': reverse("batch-add")})
            except :
                return JsonResponse({'status': 'error',  'message' : 'Batch Already Exist'})
        return JsonResponse({'status' : 'Not a Valid AJAX Request'})
            


class BatchDeleteView(View):
    def get(self, request, pk=None):
        batch = get_object_or_404(Batch, pk=pk)
        batch.delete()       
        return JsonResponse({'status':'success', 'id':pk, 'module': 'Batch'})      
      
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
             
#===================STUDENT PROFILE VIEW BEGINS HERE ==============================
class StudentProfileAddView(View):
    def get(self, request):      
         form = StudentProfileForm()
         student_profile = StudentProfile.objects.all().order_by('students_name')
         
        
         context = {
             'form': form,
             'table_name': student_profile,
         }
         return render(request,"marksheet/student-profile/add.html", context)

    def post(self, request):
         if request.headers.get('x-requested-with') == 'XMLHttpRequest': # Check if it's an AJAX request 
            try:
                #======GET DATA FROM POST REQUEST===========
                students_name = request.POST.get("students_name")
                regn_no = request.POST.get("regn_no")
                roll_no = request.POST.get("roll_no")
                mobile_no = request.POST.get("mobile_no")
                alternate_no = request.POST.get("alternate_no")
                email_address = request.POST.get("email_address")
                #===========================================


                instance = StudentProfile(students_name=students_name, regn_no=regn_no, roll_no=roll_no, mobile_no=mobile_no, alternate_no=alternate_no, email_address=email_address)                
                instance.save()
                return JsonResponse({'status': 'success', 'id': instance.id, 'Students Name': instance.students_name, 'Regn No': instance.regn_no, 'Roll No': instance.roll_no, 'Mobile No': instance.mobile_no, 'Email': instance.email_address, 'redirect_url': reverse('student-profile-index')})
            except :
                return JsonResponse({'status': 'error',  'message' : 'Roll Number/Regn Number/Email Address Already Exist'})
            return JsonResponse({'status' : 'Not a Valid AJAX Request'})
        
   
class StudentProfileView(TemplateView):
    template_name="marksheet/student-profile/index.html"

    def get_context_data(self, **kwargs):
        pass


   
#===================STUDENT PROFILE VIEW BEGINS ENDS HERE ==============================

