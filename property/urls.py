from django.urls import path
from . import views 
urlpatterns = [ 
    path('properties/',views.PropertiesViews.as_view(),name="properties"),
    path('properties/<int:property_id>',views.PropertiesViews.as_view(),name="properties"),
    path('property/<int:property_id>',views.PropertyViews.as_view(),name="property"),
    path('enquiry/',views.EnquiryView.as_view(),name="enquiry"),
    path('deletedata/<int:id>',views.Deletedata,name="Deletedata"),
    ]