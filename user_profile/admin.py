from django.contrib import admin
from user_profile.models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display =('first_name', 'last_name','email','address','mobile','dob' ,'about','user_img')

admin.site.register(UserProfile,UserProfileAdmin)