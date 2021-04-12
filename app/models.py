from django.db import models
from django.contrib.auth.models import User


class user(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_profile_completed = models.BooleanField(default=False)
