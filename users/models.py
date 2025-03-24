from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    AADHAR_CHOICES = (
        ('User', 'User'),
        ('Employee', 'Employee'),
    )
    aadhar_number = models.CharField(max_length=12, unique=True)
    phone_number = models.CharField(max_length=10)
    town_name = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    mandal = models.CharField(max_length=100)
    user_type = models.CharField(max_length=10, choices=AADHAR_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

### Step 4: Create Problem Model
class Problem(models.Model):
    SECTOR_CHOICES = [
        ('muncipal', 'muncipal'),
        ('electricity', 'electricity'),
        ('Pollution', 'Pollution'),
        ('environment', 'emviromment'),
        ('health','health'),
        ('education','education'),
        ('transport','transport'),

        ('Others', 'Others'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES)
    description = models.TextField()
    image = models.ImageField(upload_to='problem_images/', blank=True, null=True)
    mandal = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')
    submission_date = models.DateTimeField(auto_now_add=True)
