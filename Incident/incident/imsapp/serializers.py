from rest_framework.serializers import *
from rest_framework import serializers
from imsapp.models import * 

class UserSerializer(ModelSerializer):
    class Meta:
        model=MyUser
        fields="__all__"

class EmployeeSerializer(ModelSerializer):
    user_id=UserSerializer()
    class Meta:
        model=Employee
        fields="__all__"

class EmployeeProfile(ModelSerializer):
    Firstname=serializers.CharField(source="user_id.first_name")
    Lastname=serializers.CharField(source="user_id.last_name")
    Email=serializers.CharField(source="user_id.email")
    Department=serializers.CharField(source="designation_id.dep_id.name")
    class Meta:
        model=Employee
        fields=["job_title" , "id" , "designation_id" , "phone_no" , "Firstname" ,"Lastname" , "Email","Department"]



class DesignationSerializer(ModelSerializer):
    class Meta:
        model=Designation
        fields="__all__"


class PasswordResetEmailSerializer(Serializer):
    email = serializers.EmailField()