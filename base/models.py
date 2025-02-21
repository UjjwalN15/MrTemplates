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
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        # Skip role field for superuser
        extra_fields.setdefault("role", None)

        # Check that is_staff and is_superuser are True for superusers
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        # Create the superuser (ignoring the role field)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = models.CharField(max_length=225, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225)
    role = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name="custom_user_roles",
        default=3,
        null=True,
        blank=True,
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


from django.db import models
from base.models import User

class Package(models.Model):
    BASIC = "basic"
    MID_LEVEL = "mid level"
    ADVANCED = "advanced"
    PACKAGE_TYPES = [
        (BASIC, "Basic"),
        (MID_LEVEL, "Mid Level"),
        (ADVANCED, "Advanced"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    package_duration = models.CharField(max_length=255, null=True, blank=True)
    package_type = models.CharField(max_length=255, choices=PACKAGE_TYPES)
    is_active = models.BooleanField(default=False)

    def update_package_expiry(self):
        print(f"Updating package expiry for type: {self.package_type}")
        if self.package_type == "basic":
            self.package_duration = "1 year"
        elif self.package_type == "mid level":
            self.package_duration = "2 years"
        elif self.package_type == "advanced":
            self.package_duration = "3 years"

    def save(self, *args, **kwargs):
        # Call update_package_expiry before saving
        self.update_package_expiry()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Theme(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="theme_images/")
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    
    url = models.URLField()

    def __str__(self):
        return self.name




class StoreCategory(models.Model):
    name = models.CharField(max_length=255)


class Store(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    theme_id = models.ForeignKey(Theme, on_delete=models.CASCADE)
    store_category_id = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    store_logo = models.ImageField(upload_to="store_logo/")
    store_description = models.TextField()


class Payment(models.Model):
    PAYMENT_METHODS = [
        ("Esewa", "Esewa"),
        ("Khalti", "Khalti"),
        ("IME Pay", "IME Pay"),
        ("Bank Transfer", "Bank Transfer"),
        ("Cash On Delivery", "Cash On Delivery"),
    ]
    PAYMENT_STATUS = [
        ("Paid", "Paid"),
        ("Unpaid", "Unpaid"),
        ("Pending", "Pending"),
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    package_id = models.ForeignKey(Package, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHODS)
    payment_status = models.CharField(
        max_length=255, choices=PAYMENT_STATUS, default="Unpaid"
    )
    created_at = models.DateTimeField(auto_now_add=True)
