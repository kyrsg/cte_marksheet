from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
class UserModelAdmin(UserAdmin):
    filter_horizontal =()
    list_filter=()
    fieldsets=()

admin.site.register(User, UserModelAdmin)
