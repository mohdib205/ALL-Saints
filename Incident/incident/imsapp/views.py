from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail

@api_view(["GET"])
def users(request):
    print("")
    object=MyUser.objects.get(pk=1)
    print(object.employee.job_title)
    ser=UserSerializer(object)
    response=ser.data
    response["job"]=object.employee.job_title
    return Response(response)

@api_view(["GET"])
def employee_v(request):
    objects=Employee.objects.all()
    ser=EmployeeSerializer(objects, many=True)
    print(ser.data)
    print("\n"*3)
    data=[]
    for d in ser.data:
        response={}
        response["id"]=d["id"]
        response["job_title"]=d["job_title"]
        response["phone_no"]=d["id"]
        response["first_name"]=d["user_id"]["first_name"]
        response["email"]=d["user_id"]["email"]
        print(d)
        data.append(response)
        print("\n"*3)
    return Response(data)

@api_view(["GET"])
def employee_v2(request):
    objects=Employee.objects.all()
    ser=EmployeeProfile(objects, many=True)
    return Response(ser.data)

@api_view(["GET" , 'POST'])
def raise_ticket(request):
    if request.method=='GET':
        objects=IncidentTicket.objects.all()
        ser=IncidentTicketSerializer(objects, many=True)
        return Response(ser.data)
    
    if request.method=='POST':
        data=request.data
        tick=IncidentTicketSerializer(data=data)
        if tick.is_valid():
            tick.save()
            return Response("Ticket Raised")
        return Response(tick.errors)
    

@api_view(["GET"])
def Designation_v(request):
    objects=Designation.objects.all()
    ser=DesignationSerializer(objects, many=True)
    response=ser.data
    for obj,res in zip(objects, response):
        employess=obj.designations.all()
        empSer=EmployeeSerializer(employess, many=True)
        print("\n"*4)
        print(list(map(lambda x:x["id"] ,empSer.data )))
        res["employees"]=list(map(lambda x:x["id"] ,empSer.data ))  
    return Response(ser.data)




# @api_view(['PATCH'])
# def reset_passwordview(request, token=None, uid=None):
#     if request.method == 'PATCH':
#         password = request.data.get("password")
#         if token is None or uid is None or password is None:
#             return Response({"message": "Missing data"})

#         try:
#             pk = urlsafe_base64_decode(uid).decode()
#             user = User.objects.get(pk=pk)
#             if not PasswordResetTokenGenerator().check_token(user, token):
#                 return Response({"message": "The reset token is invalid"})
            
#             user.set_password(password)
#             user.save()
#             return Response({"message": "Password reset successfully"}, )
#         except User.DoesNotExist:
#             return Response({"message": "User not found"})
#         except Exception as e:
#             return Response({"message": str(e)})