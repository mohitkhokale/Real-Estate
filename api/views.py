
from rest_framework.settings import api_settings 
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import viewsets , filters
from django.contrib.auth.models import User

from property.models import Enquiry, Property
from . import serializers
# Create your views here.

class LoginVew(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.filter(is_superuser=False,is_staff=False)    


class PropertyViews(viewsets.ModelViewSet):
    serializer_class = serializers.PropertySerializer
    queryset = Property.objects.all()
 

class EnquiryViews(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = serializers.EnquirySerializer
    queryset = Enquiry.objects.all()
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ('enquiry_description',"location",'requirement_type')
    ordering_fields = ['id']