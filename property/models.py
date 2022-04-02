from datetime import datetime
from secrets import choice
from django import forms
from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from user_profile.models import UserProfile
 
# Create your models here.
class Property(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    prop_name = models.CharField(max_length=255)
    prop_img = models.ImageField(max_length=255)
    prop_area = models.CharField(max_length=255)
    status_choices = (
        ('For_Sale', 'For Sale'),
        ('Not_Available', 'Not Available'),    
        ('Sold', 'Sold'),    
    )
    prop_status = MultiSelectField("Status", choices=status_choices, default=False)
    features_choices = (
        ('SWIMMING_POOL','SWIMMING POOL'),
        ('3_STORIES','3 STORIES'),
        ('JOG_PATH 2','JOG PATH'),
        ('2_LAWN','2 LAWN'),
        ('BIKE_PATH','BIKE PATH'),
    )
    prop_price =models.IntegerField()
    prop_features= MultiSelectField('Features', choices=features_choices, default=False)
    state_choices = (
        ("Maharashtra","Maharashtra"),
        ("Madhya_Pradesh","Madhya Pradesh"),
    )
    prop_state = models.CharField(max_length=80,choices=state_choices)
    
    city_choices = (
        ("Pune","Pune"),
        ("Nagpur","Nagpur"),
        ("Ujjain","Ujjain"),
        ("Indore","Indore")
    )
    prop_city = models.CharField(max_length=80,choices=city_choices)
    prop_description = models.CharField(max_length=255)
    agent_name = models.CharField(max_length=255)
    agent_contact = models.CharField(max_length=12)
    agent_about = models.CharField(max_length=255)
    agent_email = models.CharField(max_length=255)

    def __str__(self):
        return self.prop_name


class Enquiry(models.Model):
 
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    enquiry_description = models.CharField(max_length=255)
    date_of_enquiry = models.DateTimeField(default=datetime.now())
    requirement_type =models.CharField(max_length=10)
    # How long are you planing to stay?: 1 month / 3 month / 1 Year / Not Sure how long
    duration_select = ( 
        ('1 Month','1 Month'),
        ('3 Month','3 Month'),
        ('1 Year','1 Year'),
        ('Not Sure how long','Not Sure How Long'),
    )
    duration = MultiSelectField("Duration of Stay",choices=duration_select,default=None)
    property_type_select = ( 
        ('Raw Land','Raw Land'),
        ('Lot in a Development','Lot in a Development'),
        ('Single Family Home','Single Family Home'),
        ('Other','Other'),
    )
    property_type = MultiSelectField("Property Type",choices=property_type_select,default=None)
    
    location_select = ( 
        ('In Town','In Town'),
        ('Farm or Ranch','Farm or Ranch'),
        ('Ocean View','Ocean View'),
        ('Beachfront','Beachfront'),
        ('Other','Other')
    )
    location = MultiSelectField("Location",choices=location_select,default=None)
    
    budget_select = ( 
        ('0 - 50k','0 - 50k'),
        ('50k - 5L','50k - 5L'),
        ('5L-15L','5L-15L'),
        ('15L - 1Cr','15 L - 1Cr'),
     )
    Budget = MultiSelectField("Budget",choices=budget_select,default=None)

    user_id = models.CharField(max_length=5,default='123')
    user_name = models.CharField(max_length=5,default='123')
 
    questions = models.CharField(max_length=255,blank=True, null=True)
      
    def __str__(self):
        return self.enquiry_description