from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.IndexView.as_view(), name="marksheet-index"),
    path("register/", views.register, name="register"), 
    path("login/", views.LoginView.as_view(), name="login"),
    path("status/", views.StatusView.as_view(), name="status"),
    path("organization-setup/", views.OrganizationView.as_view(), name="organization-setup"),

    #==========SUBJECT MODULE URL SETTINGS================ 
    path("subject/index/", views.SubjectAddView.as_view(), name="subject-add"),
    path("subject/edit/<int:pk>", views.SubjectEditView.as_view(), name="subject-edit"),
    path("subject/delete/<int:pk>", views.SubjectDeleteView.as_view(), name="subject-delete"),
    #====================ENDS HERE========================


    #==========SEMESTER MODULE URL SETTINGS================ 
    path("semester/index/", views.SemesterAddView.as_view(), name="semester-add"),
    path("semester/edit/<int:pk>", views.SemesterEditView.as_view(), name="semester-edit"),
    path("semester/delete/<int:pk>", views.SemesterDeleteView.as_view(), name="semester-delete"),
    #====================ENDS HERE========================


    #=============BATCH MODULE URL SETTINGS================ 
    path("batch/index/", views.BatchAddView.as_view(), name="batch-add"),
    path("batch/edit/<int:pk>", views.BatchEditView.as_view(), name="batch-edit"),
    path("batch/delete/<int:pk>", views.BatchDeleteView.as_view(), name="batch-delete"),
    #====================ENDS HERE========================   
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
