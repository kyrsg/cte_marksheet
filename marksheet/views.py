from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .forms import UserForm, OrganizationForm
from .models import User, Organization
from django.contrib import messages, auth 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView

# Create your views here.

class IndexView(View):
    def get(self, request):
        context = {
            'active': 'active',
        }
        return render(request, "marksheet/index.html", context)

    def post(self, request):
        pass

class LoginView(TemplateView):
    template_name="marksheet/login.html"
    
class StatusView(TemplateView):
   template_name="marksheet/status.html"
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["statusactive"] = 'active'
       return context

class OrganizationView(TemplateView):
   template_name="marksheet/organisation.html"

   def get_context_data(self, **kwargs):
       data = Organization.objects.get(pk=3)
       context = {
           "heads": data.heads,
           "address_1": data.address_1,
           "address_2": data.address_2,
           "address_3": data.address_3,
           "mobile_no": data.mobile_no,
           "email_address": data.email_address,
       }

       form = OrganizationForm(context)    
       context = super().get_context_data(**kwargs)
       context["form"] = form      
       return context  
   


    
    

class SubjectView(TemplateView):
   template_name="marksheet/subjects.html"
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["subjectactive"] = 'active'
       return context     

class RegisterView(View):
    def get(self, request):
        form = UserForm()
        context = {
            'form' : form,
            'registeractive': 'active',
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

            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, mobile_no=mobile_no, email=email, password=password)
            user.save()
                
            messages.success(request, "Your account has been registered successfully !!!")
                # print(messages)
                # return redirect('register')
            # response = HttpResponseRedirect('register')     
            # return response



