# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Company(models.Model):
    '''
    id:公司编号
    name:公司编号
    address:公司地址
    logo：公司logo
    description:公司简介
    createdate:公司创建时间
    createby:公司创建者
    code:公司社会信用统一代码
    cope:公司经营范围
    status：公司状况
    fatercompany:父级公司
    '''
    
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', blank=True, null=True)
    createby = models.CharField(db_column='createBy', max_length=255, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    scope = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    fathercompany = models.IntegerField(db_column='fatherCompany', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'company'


class Department(models.Model):
    '''
    id:主键
    name:部门名称
    address:部门所在地址
    admin:部门管理员
    description:部门简介
    logo:部门图标
    company：部门所属公司
    fatherdepartment:直属上级部门
    type:部门类型
    '''
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    admin = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    fatherdepartment = models.IntegerField(db_column='fatherDepartment', blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'department'

class Project(models.Model):
    '''
    id：项目编号
    name:项目名称
    price:项目造价
    address:项目地址
    description:项目简介
    startdate:进场时间
    enddate:竣工时间
    image:项目图片
    remark:备注
    '''
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)
    remark = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'project'

class ProjectRole(models.Model):
    '''
    id:关系编号
    department:项目承建部门
    role:项目所在部门角色
    project:项目名称
    '''
    id = models.IntegerField(primary_key=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    project = models.ForeignKey(Project, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'projectrole'
