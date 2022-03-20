# Generated by Django 3.2 on 2022-02-20 16:06

from django.db import migrations
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

def create_dev_superuser(*args, **kwargs):
    """Create def superuser if DEBUG is on"""
    if settings.DEBUG:
        DEV_ADMIN = {"username": "admin", "password": "admin"}
        User.objects.create_superuser(**DEV_ADMIN)


class Migration(migrations.Migration):

    dependencies = []

    operations = [migrations.RunPython(create_dev_superuser)]
    