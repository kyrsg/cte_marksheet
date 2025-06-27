from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.IndexView.as_view()), name="marksheet-index"),
    path("register/", login_required(views.RegisterView.as_view()), name="register"), 
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),   
    path("organization-setup/",  login_required(views.OrganizationView.as_view()), name="organization-setup"),

    #==========SUBJECT MODULE URL SETTINGS================ 
    path("subject/index/",  login_required(views.SubjectAddView.as_view()), name="subject-add"),
    path("subject/edit/<int:pk>",  login_required(views.SubjectEditView.as_view()), name="subject-edit"),
    path("subject/delete/<int:pk>",  login_required(views.SubjectDeleteView.as_view()), name="subject-delete"),
    #====================ENDS HERE========================


    #==========SEMESTER MODULE URL SETTINGS================ 
    path("semester/index/",  login_required(views.SemesterAddView.as_view()), name="semester-add"),
    path("semester/edit/<int:pk>",  login_required(views.SemesterEditView.as_view()), name="semester-edit"),
    path("semester/delete/<int:pk>",  login_required(views.SemesterDeleteView.as_view()), name="semester-delete"),
    #====================ENDS HERE========================


    #=============BATCH MODULE URL SETTINGS================ 
    path("batch/index/",  login_required(views.BatchAddView.as_view()), name="batch-add"),
    path("batch/edit/<int:pk>",  login_required(views.BatchEditView.as_view()), name="batch-edit"),
    path("batch/delete/<int:pk>",  login_required(views.BatchDeleteView.as_view()), name="batch-delete"),
    #====================ENDS HERE========================   
    
    #=============STUDENT PROFILE MODULE URL SETTINGS================ 
    path("student-profile/index/",  login_required(views.StudentProfileView.as_view()), name="student-profile-index"),
    path("student-profile/add/",  login_required(views.StudentProfileAddView.as_view()), name="student-profile-add"),
    path("student-profile/edit/<int:pk>",  login_required(views.BatchEditView.as_view()), name="student-profile-edit"),
    path("student-profile/delete/<int:pk>",  login_required(views.BatchDeleteView.as_view()), name="student-profile-delete"),
    #====================ENDS HERE========================  

    #=============MARKSHEET MODULE URL SETTINGS================ 
    path("marksheet/index/",  login_required(views.BatchAddView.as_view()), name="marksheet-add"),
    path("marksheet/edit/<int:pk>",  login_required(views.BatchEditView.as_view()), name="marksheet-edit"),
    path("marksheet/delete/<int:pk>",  login_required(views.BatchDeleteView.as_view()), name="marksheet-delete"),
    #====================ENDS HERE========================  

    path('get_filtered_data/', views.get_filtered_data, name='get_filtered_data'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
