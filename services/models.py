from django.db import models



class Services(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    service = models.CharField(max_length=100, blank=False, default='')
    image = models.TextField(blank=True,default='')
    description = models.TextField(blank=True,default='')
   
    class Meta:
        ordering = ('created',)