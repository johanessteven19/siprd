from django.db import models

# Create your models here.
class Admins(models.Model):
    admin_id = models.CharField(max_length=20, primary_key=True)
    admin_name = models.CharField(max_length=30)

class Users(models.Model):
    users_id = models.CharField(max_length=20, primary_key=True)
    users_name = models.CharField(max_length=30)
    users_status = models.CharField(max_length=30)
