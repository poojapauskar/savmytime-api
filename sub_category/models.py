from django.db import models


from django.contrib.postgres.fields import ArrayField

class Sub_category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    sub_category = models.CharField(max_length=100, blank=False, default='')
    category_id = models.CharField(max_length=100, blank=False, default='')
    
   
    class Meta:
        ordering = ('created',)