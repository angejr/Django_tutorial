from django.db import models

# Create your models here.

# When modifying this file
# > python manage.py makemigrations
# > python manage.py migrate


class Product (models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default="this is cool")