from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


def validate_number(number):
    if len(number) != 11 or not number.isdigit():
        raise ValidationError ('عفوا رقم التليفون هذا غير صحيح')

class User(AbstractUser):
    full_name=models.CharField(max_length=120)
    phone=models.CharField(max_length=75,validators=[validate_number])
    image=models.ImageField(upload_to='photo_user')
    job=models.CharField(max_length=120)

    first_name=None
    last_name=None

    def __str__(self):
        return self.full_name

