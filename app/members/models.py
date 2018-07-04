from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='profile_image')
    site = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    CHOICE_GENDER = (
        ('m', '남성'),
        ('f', '여성'),
        ('n', '선택안함')
    )
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)
