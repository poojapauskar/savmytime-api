from django.db import models


from django.core.validators import RegexValidator

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    transition_id = models.CharField(max_length=100, blank=False, default='')
    order_id = models.CharField(max_length=100, blank=False, default='')
    user_id = models.CharField(max_length=100, blank=False, default='')
    status = models.CharField(max_length=100, blank=False, default='')
    required_date = models.CharField(max_length=100, blank=True, default='')
   
   
    class Meta:
        ordering = ('created',)