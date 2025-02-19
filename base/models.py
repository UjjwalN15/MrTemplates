from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Creates and returns a regular user with the given email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and returns a superuser with the given email and password."""
        # Ensure the necessary superuser flags are set
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Skip role field for superuser
        extra_fields.setdefault('role', None)

        # Check that is_staff and is_superuser are True for superusers
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        # Create the superuser (ignoring the role field)
        return self.create_user(email, password, **extra_fields)



class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Package(models.Model):
    BASIC = 'basic'
    MID_LEVEL = 'mid level'
    ADVANCED = 'advanced'
    PACKAGE_TYPES = [
        (BASIC, 'Basic'),
        (MID_LEVEL, 'Mid Level'),
        (ADVANCED, 'Advanced'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    price = models.IntegerField()
    package_type = models.CharField(max_length=255, choices=PACKAGE_TYPES)

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    role = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="custom_user_roles", default=3, null=True, blank=True)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email

