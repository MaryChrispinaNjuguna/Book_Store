from django.db import models

# Create your models here.
class User(models.Model):
    email=models.EmailField(max_length=30)
    password=models.PasswordField(max_length=30)
    