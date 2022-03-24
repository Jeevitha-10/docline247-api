from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CategoryManager, DoctorManager


class User(AbstractUser):

    class Meta:
        db_table = 'dl_users'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='categories/')

    objects = CategoryManager()

    class Meta:
        db_table = 'dl_categories'

    def __str__(self) -> str:
        return self.name


class Doctor(models.Model):

    class Gender(models.TextChoices):
        M = 'M'
        F = 'F'
        T = 'T'

    YEAR_CHOICES = []
    for year in range(1980, datetime.now().year+1):
        YEAR_CHOICES.append((year, year))

    name = models.CharField(max_length=128, unique=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    year_of_employment = models.IntegerField(choices=YEAR_CHOICES)
    profile_pic = models.ImageField(upload_to='doctors/')

    objects = DoctorManager()

    class Meta:
        db_table = 'dl_doctors'

    def __str__(self) -> str:
        return self.name
