from django.db import models

class Users(models.Model):
    acc_img = models.ImageField()
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=10)


    def __str__(self):
        return self.first_name
    