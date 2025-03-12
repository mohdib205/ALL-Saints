from django.shortcuts import render
from drfapp.models import *
from drfapp.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(["GET", "POST","PUT","PATCH","DELETE"])
def product_view(request):
    if request.method=="GET":
        products=Products.objects.all()
        ser=ProductSerializer(products, many=True)
        print(ser.data)
        return Response(ser.data)
    if request.method=="POST":
        print(request.data)
        post_data=request.data
        ser=ProductSerializer(data=post_data)
        if ser.is_valid():
            ser.save()
            return Response("product added successfully")
        return Response(ser.errors)
    if request.method=="PUT":
        id=request.data.get("id")
        obj=Products.objects.get(id=id)
        ser=ProductSerializer(obj, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    if request.method=="PATCH":
        id=request.data.get("id")
        obj=Products.objects.get(id=id)
        ser=ProductSerializer(obj, data=request.data , partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    if request.method=="DELETE":
        id=request.data["id"]
        obj=Products.objects.get(id=id)
        obj.delete()
        return Response("data deleted successfully")

#PUT and PATCH


@api_view(["GET","POST"])
def order_view(request):
    if request.method=="GET":
        orders=Orders.objects.all()
        order_ser=OrderSerializer(orders, many=True)
        print(order_ser.data)
        return Response(order_ser.data)
    if request.method=="POST":
        print(request.data)
        post_data=request.data
        print(post_data.get("product"))
        prod_obj=Products.objects.get(id=post_data.get("product"))
        print(prod_obj.stock)
        order_ser=OrderSerializer(data=post_data)
        if order_ser.is_valid():
            order_ser.save()
            prod_obj.stock-=post_data.get("quantity")
            prod_obj.save()
            
            return Response("data inserted successsfully")
        return Response(order_ser.errors)



@api_view(["GET"])
def productSort(request):
    products= Products.objects.all().order_by("-stock")
    ser=ProductSerializer(products, many=True)
    return Response(ser.data)


@api_view(["GET"])
def productFilter(request , value):
    products= Products.objects.filter(stock=value)
    ser=ProductSerializer(products, many=True)
    return Response(ser.data)

#File field /Image Field

@api_view(["GET","POST"])
def carousal_view(request):
    if request.method=="GET":
        products= Carousal.objects.all()
        ser=CarousalSerializer(products, many=True)
        return Response(ser.data)
    if request.method=="POST":
        data=request.data
        print(data)
        ser=CarousalSerializer(data=data)
        if ser.is_valid():
            ser.save()
            return Response("data added")
        return Response(ser.errors)





