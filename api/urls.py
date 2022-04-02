from django.urls import path , include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('users',views.UserView)
router.register('property',views.PropertyViews)
router.register('enquiry',views.EnquiryViews)

urlpatterns = [ 
    path('login',views.LoginVew.as_view()),
    path('',include(router.urls)),

]