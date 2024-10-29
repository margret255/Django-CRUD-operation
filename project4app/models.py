from django.db import models

# defining table as required

class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.name