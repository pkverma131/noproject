from django.utils import timezone
from django.db import models
from lead.models import Country
# from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo =  models.FileField(null=True, blank=True)
    company = models.CharField(max_length=100)
    origin = models.ForeignKey(Country, on_delete=models.CASCADE)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class ApplianceType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Specification(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Appliance(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class ApplicianceSpecificationAsso(models.Model):
    appliances_id = models.IntegerField()
    specification_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Seller(models.Model):
    name = models.CharField(max_length=100)
    channel= models.CharField(max_length=100)
    site_url = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class ApplianceSellerPriceAsso(models.Model):
    appliance_id = models.IntegerField()
    seller_id = models.IntegerField()
    price = models.FloatField()
    listing_url = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class Offer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    desccription = models.CharField(max_length=200)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

class OfferAttribute(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    
class OfferAttributeAsso(models.Model):
    offer_id = models.IntegerField()
    offer_attribute_id = models.IntegerField()
    created_by = models.IntegerField()
    created_at = models.DateTimeField()
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
