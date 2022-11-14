from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None
    email = models.EmailField(null=False, blank=False)
    is_active = models.BooleanField(null=True, blank=True,default=1)
    last_login = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


