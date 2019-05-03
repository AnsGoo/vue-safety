from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.
class CMDB(models.Model):
    choices=(
        (0,'worker'),
        (1,'hava_server'),
        (2,'jenkins_server')
    )
    ip = models.CharField(max_length=64,unique=True)
    device_type = models.CharField(max_length=10,choices=choices,default=0)
    port = models.CharField(max_length=64)
    creator=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    group = models.ForeignKey(Group,on_delete=models.DO_NOTHING)
    hostname = models.CharField(max_length=64, null=True)
    status = models.BooleanField(default=True)
    addtime = models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=50)
    rsa_pub=models.CharField(max_length=255,null=True)
    authentication=models.CharField(max_length=10,choices=(('0','sess'),('1','password')))

    def __unicode__(self):
        return self.ip