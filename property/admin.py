from django.contrib import admin
from . models import Property , Enquiry

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('prop_name','agent_name', 'prop_description','prop_img')
admin.site.register(Property,PropertyAdmin)

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('enquiry_description','date_of_enquiry', 'requirement_type','duration','user_id','user_name')

admin.site.register(Enquiry,EnquiryAdmin)