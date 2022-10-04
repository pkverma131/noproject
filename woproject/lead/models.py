from django.utils import timezone
from django.db import models
# from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class State(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class City(models.Model):
    state_id = models.IntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Lead(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    pincode = models.IntegerField()
    city = models.IntegerField()
    state = models.IntegerField()
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
