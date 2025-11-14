

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    GENDER_CHOICES = [
        ('Nam', 'Nam'),
        ('Nữ', 'Nữ'),
    ]
    MEMBERSHIP_CHOICES = [
        ('', 'Không có'),
        ('Gold', 'Gold'),
        ('Diamond', 'Diamond'),
        ('VIP', 'VIP'),
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=15)
    membership = models.CharField(max_length=50,
                                  choices=MEMBERSHIP_CHOICES,
        blank=True,   # không bắt buộc điền
        null=True)

    def __str__(self):
        return self.user.username
