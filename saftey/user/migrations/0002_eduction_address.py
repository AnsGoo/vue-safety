# Generated by Django 2.1.2 on 2018-12-03 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eduction',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
