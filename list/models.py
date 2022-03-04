from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birthdate = models.DateField()
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

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

