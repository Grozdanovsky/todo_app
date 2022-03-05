from django.db import models
from django.conf import settings
from django.contrib import admin
# Create your models here.

class Customer(models.Model):
    phone = models.CharField(max_length=255)
    birthdate = models.DateField()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.user.first_name} {self.user.last_name}'

        
    @admin.display(ordering ='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering= 'user__last_name')
    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email


    class Meta:
        ordering = ['user__last_name']

class TodoList(models.Model):

    STATUS_UNFINISHED = 'U'
    STATUS_FINISHED = "F"
    STATUS_CHOICES = [
        (STATUS_UNFINISHED, 'Unfinished'),
        (STATUS_FINISHED, 'Finished')
    ]

    item = models.CharField(max_length=255)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES, default=STATUS_UNFINISHED)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.item

