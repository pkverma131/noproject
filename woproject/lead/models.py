from django.db import models

class Country:
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

class State(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class City(models.Model):
    state_id = models.IntegerField()
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class Lead(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    pincode = models.IntegerField()
    city = models.IntegerField()
    state = models.IntegerField()
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()
