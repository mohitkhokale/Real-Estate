from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.HomePage.as_view(),name='index'),
    path('contact',views.Contact,name='contact'),
    path('properties/<int:property_id>',views.HomePage.as_view(),name="properties"),

] 