from django.db import models


owner = models.ForeignKey('auth.User', related_name='create')
highlighted = models.TextField()

class Get_details(models.Model):
 created = models.DateTimeField(auto_now_add=True)
 

 class Meta:
  ordering = ('created',)

