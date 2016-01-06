from django.db import models

from django.contrib.postgres.fields import ArrayField

class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, blank=False, default='')
    service_id = models.CharField(max_length=100, blank=False, default='')
    
   
    class Meta:
        ordering = ('created',)