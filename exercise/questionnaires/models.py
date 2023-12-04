from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth.models import User


# Custom User Model
class CustomUser(AbstractUser):
    # Your additional fields and configurations for the user model

    # Override the groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')


# Other Models
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    
class Questionnaire(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Response(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=100)  # Field for user type, e.g., 'admin' or 'customer'
    # Add other fields as needed

    def __str__(self):
        return self.user.username  # Customize how UserProfile objects are displayed
