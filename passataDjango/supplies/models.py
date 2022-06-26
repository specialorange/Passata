from django.db import models
from batch.models import VolumeUnit, WeightUnit


class Location(models.Model):
    name = models.CharField(max_length=50, default="Location Name Not Set")
    sub_name = models.CharField(
        max_length=50, blank=True, null=True, default="Additional Name Not Set"
    )
    address_line1 = models.CharField(max_length=45, default="Address Not Set")
    address_line2 = models.CharField(max_length=45, blank=True)
    postal_code = models.CharField(max_length=15, default="ZIPCode Not Set")
    city = models.CharField(max_length=50, default="City Not Set")
    state_province = models.CharField(max_length=40, default="State Not Set")
    country = models.CharField(max_length=40, default="USA")
    corporate = models.BooleanField(null=True)
    contact_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11, default="17042123123")

    def __str__(self):
        return self.name

    def full_address(self):
        return "%s, %s, %s, %s" % (
            self.address_line1,
            self.city,
            self.state_province,
            self.postal_code,
        )

    def encode_url(self):
        return urllib.parse.quote_plus(self.full_address())

    def google_link(self):
        return "{}{}".format(
            "https://www.google.com/maps/search/?api=1&query=", self.encode_url()
        )

    class Meta(object):
        verbose_name_plural = "Locations"
        unique_together = (
            "name",
            "address_line1",
            "address_line2",
            "postal_code",
            "city",
            "state_province",
            "country",
        )


class Retailer(models.Model):
    name = models.CharField(max_length=100)
    location = models.ManyToManyField(Location, related_name="retail_locations")

    def __str__(self):
        return self.name


class Supply(models.Model):
    name = models.CharField(max_length=50)
    volume_amount = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    count = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    volume_unit = models.ForeignKey(
        VolumeUnit,
        on_delete=models.DO_NOTHING,
        related_name="supply",
        blank=True,
        null=True,
    )
    weight_unit = models.ForeignKey(
        WeightUnit,
        on_delete=models.DO_NOTHING,
        related_name="supply",
        blank=True,
        null=True,
    )
    retailer = models.ForeignKey(
        Retailer,
        on_delete=models.DO_NOTHING,
        related_name="supply",
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.count} {self.volume_unit} {self.weight_unit}"

    class Meta:
        verbose_name_plural = "Supplies"


class Season(models.Model):
    name = models.CharField(max_length=50)
    supply_list = models.ManyToManyField(Supply, related_name="season", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
