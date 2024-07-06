from django.db import models
from django.utils import timezone
# Create your models here.
class todo(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    details = models.TextField(max_length=1000,null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task