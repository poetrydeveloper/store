from django.db import models

class Tools(models.Model):
    code = models.CharField(max_length=100)
    name = models.TextField(max_length=250)
    desc = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    def __str__(self):
			  return self.title