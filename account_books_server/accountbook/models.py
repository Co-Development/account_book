from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    avatar_url = models.CharField(max_length=255)
    eat_count = models.IntegerField()
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'name': self.name,
            'avatar_url': self.avatar_url,
            'type': self.type
        }


class ExpensesNotes(models.Model):
    """消费记录model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField()
    money = models.IntegerField(default=0)
    note = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.create_time}, {self.user.name}'

    def to_dict(self):
        return {
            'user': self.user.to_dict(),
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'money': self.money,
            'note': self.note
        }
