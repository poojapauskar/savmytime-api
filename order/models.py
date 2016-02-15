from django.db import models


from django.core.validators import RegexValidator

class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    order_id = models.CharField(max_length=100, blank=False, default='')
    user_id = models.CharField(max_length=100, blank=False, default='')
    status = models.CharField(max_length=100, blank=False, default='')
   
   
    class Meta:
        ordering = ('created',)