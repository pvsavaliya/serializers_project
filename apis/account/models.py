from distutils.text_file import TextFile
from pyexpat import model
from tkinter import CASCADE, Image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import PasswordInput

# Create your models here.

class UserDetail(AbstractUser):
    
    # TYPE_CHOICES = (
    #   ("Pharmacist", "pharmacist"),
    #   ("Admin", "admin"),
    #   ("Doctor", "doctor"),
    #   ("Receptionist", "receptionist"),
    # )
    userID          = models.AutoField(primary_key=True, unique=True)
    role            = models.CharField(max_length=128, null=True, blank=True)
    username        = models.CharField(max_length=128,unique=True, null=False)
    first_name      = models.CharField(max_length=128, null=True)
    last_name       = models.CharField(max_length=128, null=True)
    dob             = models.DateField(max_length=128, null=True)
    email           = models.EmailField(max_length=128, null=False, unique=True)
    userphone       = models.CharField(max_length=10, null=True)
    useraddress     = models.CharField(max_length=200, null=True,blank=True)
    password        = models.CharField(max_length=255, null=False)
    isDeleted       = models.BooleanField(default = False,null=True)
    Token           = models.TextField(null=True)
    Image           = models.FileField(upload_to='message/%Y/%m/%d/', null=True, blank=True)
    # comment         = models.ManyToManyField(Comment ) 
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

class EmailOTP(models.Model):
    email = models.CharField(max_length=128, unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    count = models.IntegerField(default=0)
    validated = models.BooleanField(default= False)
    otp_session_id = models.CharField(max_length=120, null=True, default = "")

class Comment(models.Model):
    userID  = models.AutoField(primary_key=True, unique=True)
    comment = models.TextField()
    user = models.ForeignKey(UserDetail, on_delete = models.CASCADE, related_name="user_id")
    created         = models.DateField(auto_now_add=True)
    updated         = models.DateField(auto_now=True)
    isDeleted       = models.BooleanField(default = False,null=True)
    def __str__(self):
        return str(self.user_id) 

class tag(models.Model):
    tag = models.ManyToManyField(UserDetail)
    text = models.CharField(max_length=100)