from django.db import models


from django.core.validators import RegexValidator

class Transition(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    transition_id = models.CharField(max_length=100, blank=False, default='')
    service_id = models.CharField(max_length=100, blank=False, default='')
    category_id = models.CharField(max_length=100, blank=False, default='')
    sub_category_id = models.CharField(max_length=100, blank=False, default='')
   
   
    class Meta:
        ordering = ('created',)