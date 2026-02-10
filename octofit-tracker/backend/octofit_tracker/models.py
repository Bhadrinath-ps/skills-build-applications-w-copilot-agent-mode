from djongo import models
from django.contrib.auth.models import AbstractUser

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    def __str__(self):
        return f"{self.user} - {self.type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    def __str__(self):
        return f"{self.team}: {self.points}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=100, blank=True, null=True)

    # Fix reverse accessor clashes by setting unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_users',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_users_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
