from django.db import models

from django.contrib.postgres.fields import ArrayField

class Cities(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, blank=False, default='')
    service_list = ArrayField(models.TextField(blank=True, default='',editable=True))
    
   
    class Meta:
        ordering = ('created',)