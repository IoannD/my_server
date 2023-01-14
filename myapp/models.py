from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=50)
    age = models.SmallIntegerField()

    def __str__(self):
        return self.user_name

    def was_user_adult(self):
        return self.age >= 18
    