from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    type = models.CharField(max_length=50,null=True)
    
class Jobseeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)   
    mobile = models.CharField(max_length=15, null=True)

class JobseekerProfile(models.Model):
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE,null=True)
    age = models.DateField(null=True)
    gender = models.CharField(max_length=15, null=True)
    qualification = models.CharField(max_length=50, null=True)
    address = models.TextField(null=True)
    pincode = models.CharField(max_length=15, null=True)
    experience = models.CharField(max_length=150, null=True)
    skills = models.CharField(max_length=100, null=True)
    image = models.ImageField(null=True)
    resume = models.ImageField(null=True)
    

class Employer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)   
    mobile = models.CharField(max_length=15, null=True) 
    
class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE,null=True)   
    image = models.ImageField(null=True) 
    gender = models.CharField(max_length=25, null=True)
    email = models.EmailField(max_length=254, null=True)
    title = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=25, null=True)
    job_type = models.CharField(max_length=25, null=True)
    description = models.CharField(max_length=55, null=True)
    companyname = models.CharField(max_length=50, null=True)
    company_description = models.CharField(max_length=55, null=True)
    website = models.CharField(max_length=15, null=True)
    fb_username = models.CharField(max_length=15, null=True)
    tw_username = models.CharField(max_length=15, null=True)
    lk_username = models.CharField(max_length=15, null=True)
    logo = models.ImageField(null=True)
    published_on = models.DateField(null = True)
    vacancy = models.CharField(max_length=15, null=True)
    experience = models.CharField(max_length=15, null=True)
    salary = models.CharField(max_length=15, null=True)
    last_date = models.DateField(null=True)
    experience = models.TextField(null=True)
    
class Book(models.Model):
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE,null=True)
    job = models.ForeignKey(Job, on_delete=models.CASCADE,null=True)  
    status = models.CharField(max_length=15, null=True) 