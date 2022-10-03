from django.contrib import admin
from lead.models import Lead, City,State,Country

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    pass
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    pass
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass