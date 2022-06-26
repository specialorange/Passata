from django.contrib import admin
from supplies import models


class LocationInline(admin.TabularInline):
    model = models.Retailer.location.through
    extra = 1


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "sub_name",
        "address_line1",
        "address_line2",
        "postal_code",
        "city",
        "state_province",
        "country",
        "corporate",
        "contact_name",
        "phone_number",
    ]


@admin.register(models.Retailer)
class RetailerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        # "location",
    ]
    inlines = (LocationInline,)


@admin.register(models.Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "volume_amount",
        "count",
        "volume_unit",
        "weight_unit",
        "retailer",
    ]


@admin.register(models.Season)
class SeasonAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        # "supply_list",
    ]
