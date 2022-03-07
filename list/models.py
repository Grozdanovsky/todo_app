from django.db import models
from django.conf import settings
from django.contrib import admin

from core.models import User
# Create your models here.





class TodoList(models.Model):

    STATUS_UNFINISHED = 'U'
    STATUS_FINISHED = "F"
    STATUS_CHOICES = [
        (STATUS_UNFINISHED, 'Unfinished'),
        (STATUS_FINISHED, 'Finished')
    ]

    item = models.CharField(max_length=255)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default=STATUS_UNFINISHED)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.item

