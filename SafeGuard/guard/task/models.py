from django.db import models
from django.contrib.auth.models import User,Group
from cmdb.models import CMDB

# Create your models here.
class Task(models.Model):
    choices=(
        (0,'never'),
        (1,'hourly'),
        (2,'daily'),
        (3,'weekly'),
        (4,'monthly'),
        (5,'yearly')
    )
    name=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    addtime=models.DateTimeField(auto_now_add=True)
    command=models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField(null=True)
    frequency=models.CharField(max_length=10,choices=choices,default=0)

class AssignTask(models.Model):
    task=models.ForeignKey(Task,on_delete=models.CASCADE)
    cmdb=models.ForeignKey(CMDB,on_delete=models.CASCADE)

class Result(models.Model):
    record=models.TextField(null=True)
    measure	=models.CharField(max_length=100)
    params=models.CharField(max_length=256)
    run_time=models.DateTimeField(auto_now_add=True)
    task=models.ForeignKey(AssignTask,on_delete=models.CASCADE)
