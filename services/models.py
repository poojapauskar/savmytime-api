from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Services(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    service = models.CharField(max_length=100, blank=False, default='')
    image = models.TextField(blank=True,default='')
    description = models.TextField(blank=True,default='')
   
    class Meta:
        ordering = ('created',)