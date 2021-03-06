from django.db import models


from django.core.validators import RegexValidator





class User_data(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
    phone = models.CharField(max_length=12,validators=[phone_regex], blank=True) # validators should be a list
    email = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=100, blank=False, default='')
    
   
    class Meta:
        ordering = ('created',)