from django.urls import path,  include
from .views import *
urlpatterns = [
    path("u/", users),
    path("employee/", employee_v),
    path("emp2/", employee_v2),
    path("des/", Designation_v),
    path("tick/", raise_ticket),
]
