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


@api_view(["GET"])
def Designation_v(request):
    objects=Designation.objects.all()
    ser=DesignationSerializer(objects, many=True)
    response=ser.data
    print(type(objects))
    for obj,res in zip(objects, response):
        employess=obj.designations.all()
        empSer=EmployeeSerializer(employess, many=True)
        print("\n"*4)
        print(list(map(lambda x:x["id"] ,empSer.data )))
        res["employees"]=list(map(lambda x:x["id"] ,empSer.data ))  
    return Response(ser.data)

@api_view(["POST"])
def reset_pwordlink(request):
    if request.method=='POST':
        data=request.data
        serializer = PasswordResetEmailSerializer(data=data)
        # print(serializer)
        if serializer.is_valid():
            email = serializer.data['email']
            print(email)
            user = MyUser.objects.get(email=email)
            print(user)
            if user is None:
                print("Customer Does not Exist(of this Email)")
            elif user is not None:
                Userid=user.__dict__["User_id_id"]
                
                Userr= User.objects.get(id=Userid)
                uid = urlsafe_base64_encode(force_bytes(Userr.id))
                token= PasswordResetTokenGenerator().make_token(Userr)
                request.session['password_reset_token'] = token
                base_url = request.build_absolute_uri('/')[:-1]
                reset_url = f'{base_url}/reset-password/{token}/{uid}/'
                print(token)
                send_mail(
                    'Password Reset Request',
                    f'Click the following link to reset your password: {reset_url}',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )
                return Response({'message': 'Password reset email link sent succesfully ' , "reset_url":reset_url})
        return Response(serializer.errors) 


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