from django.db import models
from django.contrib.auth.models import User


class ProfileManager(models.Manager):
    def create(self, username, email, photo=None):
        """Always create User and Profile instances in tandem."""
        user = User(username=username, email=email)
        user.save()
        profile = UserProfile(user=user, photo=photo)
        profile.save()
        return profile


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/', blank=True)
    objects = ProfileManager()
