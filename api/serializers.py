from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from property.models import Enquiry, Property

'''********* we can also alter serializers **********'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id','username','first_name','last_name','password','email']
        extra_kwargs = {'password':{'write_only':True} }

    def create(self,validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password']),
        user.save()
        return user
    
    def update(self,instance,validated_data):
        print(validated_data) 
        instance.username = validated_data.get('username',instance.username)
        instance.first_name = validated_data.get('first_name',instance.first_name)
        instance.last_name = validated_data.get('last_name',instance.last_name)
        instance.email = validated_data.get('email',instance.email)
        instance.save()
        return instance 


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model=Property
        fields= '__all__'


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model=Enquiry
        fields= '__all__'