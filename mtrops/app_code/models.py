from django.db import models

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=32, unique=True)
    project_msg = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return self.project_name


class Site(models.Model):
    site_name = models.CharField(max_length=64, unique=True)
    site_msg = models.CharField(max_length=64, null=True)
    project = models.ForeignKey(to='Project', on_delete=models.DO_NOTHING)
    site_url = models.CharField(max_length=128, unique=True)
    site_depend = models.CharField(max_length=256, null=True)

    def __unicode__(self):
        return self.site_name


class Depend(models.Model):
    depend_name = models.CharField(max_length=64)
    depend_version = models.CharField(max_length=64, null=True)
    install_script = models.TextField(null=True)

    def __unicode__(self):
        return self.service_name


class CodePost(models.Model):
    post_site = models.ForeignKey(to='Site', on_delete=models.DO_NOTHING)
    post_ip = models.CharField(max_length=64)
    site_path = models.CharField(max_length=128)
    postsite_msg = models.CharField(max_length=128, null=True)
    current_version = models.CharField(max_length=64, null=True)
    version_info = models.CharField(max_length=512, null=True)
    author = models.CharField(max_length=64, null=True)
    upcode_date = models.CharField(max_length=64, null=True)
    create_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.post_site


class PostRecord(models.Model):
    CodePost = models.ForeignKey(
        to='CodePost', null=True, on_delete=models.DO_NOTHING)
    current_version = models.CharField(max_length=64, null=True)
    version_info = models.CharField(max_length=512, null=True)
    author = models.CharField(max_length=64, null=True)
    upcode_date = models.CharField(max_length=64, null=True)

    def __unicode__(self):
        return self.post_site
