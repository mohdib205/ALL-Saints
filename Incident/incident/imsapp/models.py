from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    

    
class MyUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()
    
    role = models.ForeignKey(
        Role, blank = True ,related_name="user", null = True, on_delete = models.SET_NULL
    )

    def __str__(self):
        return self.email

class Department(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    

# Designation Model

class Designation(models.Model):
    name = models.CharField(max_length = 200)
    dep_id = models.ForeignKey(Department, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user_id = models.OneToOneField(MyUser, on_delete = models.CASCADE , related_name="employee")
    designation_id = models.ForeignKey(Designation, on_delete = models.CASCADE , related_name="designations")
    job_title = models.CharField(max_length = 200)
    phone_no = models.CharField(max_length = 50)
    def __str__(self):
        return f"Employee: {self.user_id}"
    

class IncidentType(models.Model):
    name = models.CharField(max_length = 200)
    department_id = models.ForeignKey(Department, on_delete = models.CASCADE)

class ContributingFactor(models.Model):
    name = models.CharField(max_length = 200)


class DepartmentPOC(models.Model):
    department_id = models.ForeignKey(Department, on_delete = models.CASCADE , related_name="poc")
    employee_id = models.ForeignKey(Employee, on_delete = models.CASCADE , related_name="deps")

class IncidentTicket(models.Model):
    requestor_id = models.ForeignKey(Employee, on_delete = models.CASCADE)
    report_type = models.ForeignKey(IncidentType, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE , null = True , blank=True)
    occurrence_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length = 200)
    risk_level = models.CharField(max_length = 200, null = True , blank=True )
    department = models.ForeignKey(Department, on_delete = models.CASCADE, null = True, blank = True)   
    assigned_poc=models.ForeignKey(DepartmentPOC , on_delete=models.CASCADE ,  null = True , blank=True)
    contributing_factor=models.ManyToManyField("ContributingFactor" , db_table="IncidentFactor")
        


