from django.db import models
from django.contrib.auth.models import User


class UserProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="userprofile")
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    def __str__(self) -> str:
        return self.user.username