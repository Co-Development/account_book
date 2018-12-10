from django.db import models

# Create your models here.


class AccountBook(models.Model):
    """账单model"""
    create_name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    money = models.IntegerField(default=0)
    note = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=255)

    def __str__(self):
        return self.create_time

