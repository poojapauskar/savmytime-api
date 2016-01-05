from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

from django.core.validators import RegexValidator

class Service_providers(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    service_id = models.IntegerField(blank=False)
    name = models.CharField(max_length=100, blank=False, default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12}$', message="Enter country code. Phone number must be entered in the format: '919999999'.")
    phone = models.CharField(max_length=12,validators=[phone_regex], blank=False) # validators should be a list
    email = models.CharField(max_length=100, blank=False, default='')
    city = models.CharField(max_length=100, blank=False, default='')
    address = models.CharField(max_length=100, blank=False, default='')
    
   
    class Meta:
        ordering = ('created',)