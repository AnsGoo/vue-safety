#!/usr/bin/env python  
# encoding: utf-8  
from __future__ import absolute_import
import time
from django.core.mail import send_mail
from celery.utils.log import get_task_logger
from celery import shared_task
from celery import task
# from task.celery import app

# from art.utils.send_mail import pack_html, send_email

@task
def tsend_email():
#    url = "http://1000phone.com"
#    receiver = 'diyuhuan@1000phone.com'
#    content = pack_html(receiver, url)
#    # content = 'this is email content.'
#    send_email(receiver, content)
   print('send email ok!')

@task
def add(x, y):
   return x+y