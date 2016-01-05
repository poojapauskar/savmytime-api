from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

from django.contrib.postgres.fields import ArrayField

class Cities(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=100, blank=False, default='')
    service_list = ArrayField(models.TextField(blank=True, default='',editable=True))
    
   
    class Meta:
        ordering = ('created',)