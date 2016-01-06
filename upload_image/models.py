from django.db import models
import time


from pygments.formatters.html import HtmlFormatter
from pygments import highlight
import random
from random import randint


owner = models.ForeignKey('auth.User', related_name='upload_image')
highlighted = models.TextField()

# from django.conf import settings
# from django.core.files.storage import FileSystemStorage
# fs = FileSystemStorage(location=settings.STATIC_ROOT)

class Upload_image(models.Model):
    photo = models.ImageField(upload_to="/projectimg",null=True, blank=True)
    link=models.TextField(blank=True,default='')


