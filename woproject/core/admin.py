from django.contrib import admin
from core.models import Brand, ApplianceType,Specification,Appliance,ApplicianceSpecificationAsso,Seller,ApplianceSellerPriceAsso,Offer,OfferAttribute,OfferAttributeAsso

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass
@admin.register(ApplianceType)
class CityAdmin(admin.ModelAdmin):
    pass
@admin.register(Specification)
class StateAdmin(admin.ModelAdmin):
    pass
@admin.register(Appliance)
class ApplianceAdmin(admin.ModelAdmin):
    pass

@admin.register(ApplicianceSpecificationAsso)
class ApplicianceSpecificationAssoAdmin(admin.ModelAdmin):
    pass
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass
@admin.register(ApplianceSellerPriceAsso)
class ApplianceSellerPriceAssoAdmin(admin.ModelAdmin):
    pass
@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    pass
@admin.register(OfferAttribute)
class OfferAttributeAdmin(admin.ModelAdmin):
    pass
@admin.register(OfferAttributeAsso)
class OfferAttributeAssoAdmin(admin.ModelAdmin):
    pass