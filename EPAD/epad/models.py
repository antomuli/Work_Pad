from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class profile(models.Model):
    '''
    Class to define employee
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = CloudinaryField('images')
    first_name=models.CharField(max_length=500,blank=True)
    last_name=models.CharField(max_length=500,blank=True)
    position=models.CharField(max_length=500,blank=True)
    employed_on=models.DateTimeField(auto_now_add=True)

class kpis(models.Model):
    '''
    Class to define the key performance indicators
    '''
    rates_for=models.ForeignKey(User,on_delete=models.CASCADE)
    work_quality = models.IntegerField(default=1)
    attendance=models.IntegerField(default=1)
    punctuality = models.IntegerField(default=1)
    soft_skills=models.IntegerField(default=1)

class tasks(models.Model):
    '''
    Class to define employee tasks
    '''
    title=models.CharField(max_length=1000)
    task=models.TextField(max_length=5000)
    added_on=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField(auto_now_add=False)
    completed=models.BooleanField(default=False)
    assigned_to=models.ManyToManyField(User)

    def user_tasks(cls,id):
        user_tasks = cls.objects.filter(assigned_to = assigned_to)
        return user_tasks