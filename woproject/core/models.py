from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo =  models.FileField()
    company = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class ApplianceType(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class Specification(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class Appliance(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class ApplicianceSpecificationAsso(models.Model):
    appliances_id = models.IntegerField()
    specification_id = models.IntegerField()
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class Seller(models.Model):
    name = models.CharField(max_length=100)
    channel= models.CharField(max_length=100)
    site_url = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class ApplianceSellerPriceAsso(models.Model):
    appliance_id = models.IntegerField()
    seller_id = models.IntegerField()
    price = models.FloatField()
    listing_url = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class Offer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    desccription = models.CharField(max_length=200)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()

class OfferAttribute(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()
    
class OfferAttributeAsso(models.Model):
    offer_id = models.IntegerField()
    offer_attribute_id = models.IntegerField()
    created_by = models.IntegerField()
    create_at = models.DateTimeField()
    updated_by = models.IntegerField()
    updated_at = models.DateTimeField()
