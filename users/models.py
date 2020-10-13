from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
# from shop.models import Products

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    address = models.CharField(max_length=256, blank=True, null=True )
    phone_no = models.PositiveIntegerField(blank=True, null=True)
  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class UserInfo(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    

#     def __str__(self):
#         return user.email