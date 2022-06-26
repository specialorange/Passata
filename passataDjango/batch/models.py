import string
import random

from django.db import models
from django.db import IntegrityError
from django.utils import timezone


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


class PhoneNumberManager(models.Manager):
    def with_all_parts(self):
        return self.annotate(
            full_number=Concat(
                F("country_code"),
                F("area_code"),
                F("pnumber"),
                F("extension"),
                output_field=CharField(),
            )
        )


class Consumer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300, blank=True, null=True)
    phone_type = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=1, default="1")
    area_code = models.CharField(max_length=3, blank=True, null=True)
    pnumber = models.CharField(max_length=7, blank=True, null=True)
    extension = models.CharField(max_length=4, blank=True, null=True)
    objects = models.Manager()  # The default manager.
    full_number = PhoneNumberManager()

    @property
    def phone_number(self):
        if self.pnumber is not None and self.area_code is not None:
            if self.extension:
                return (
                    self.country_code
                    + self.area_code
                    + self.pnumber
                    + "+"
                    + self.extension
                )
            else:
                return self.country_code + self.area_code + self.pnumber
        else:
            return None

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    consumer = models.ForeignKey(
        Consumer,
        on_delete=models.DO_NOTHING,
        related_name="order",
    )
    fulfilled = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    volume_amount = models.DecimalField(max_digits=7, decimal_places=2)
    volume_unit = models.ForeignKey(
        "batch.VolumeUnit",
        on_delete=models.DO_NOTHING,
        related_name="order",
    )

    def __str__(self):
        return f"{self.consumer} for {self.name}"


class Chef(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class VolumeUnit(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    unit = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WeightUnit(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    unit = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    food = models.ForeignKey(
        Food,
        on_delete=models.DO_NOTHING,
        related_name="ingredient",
    )
    volume_amount = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    volume_unit = models.ForeignKey(
        VolumeUnit,
        on_delete=models.DO_NOTHING,
        related_name="ingredient",
    )
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name()

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = str(self.food)
            super().save(*args, **kwargs)

    def full_name(self):
        return f"{self.name} - {self.volume_amount}"
        # return f"{self.food} - {self.volume_amount} {self.volume_unit}"


class Recipe(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_ingredients(self):
        if self.ingredients:
            return self.ingredients.all()
            # return "%s" % " / ".join(
            #     [ingredient.name for ingredient in self.ingredients.all()]
            # )


class BasicStep(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    name = models.ForeignKey(
        BasicStep, on_delete=models.DO_NOTHING, related_name="step", null=True
    )
    initial_weight_amount = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    final_weight_amount = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    weight_unit = models.ForeignKey(
        WeightUnit,
        on_delete=models.DO_NOTHING,
        related_name="step",
    )
    order = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    chefs = models.ManyToManyField(Chef)
    batch = models.ForeignKey(
        "batch.Batch",
        on_delete=models.DO_NOTHING,
        related_name="step",
        null=True,
    )
    process = models.ForeignKey(
        "batch.Process",
        on_delete=models.DO_NOTHING,
        related_name="step",
        null=True,
    )
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order} - {self.name}"

    class Meta:
        ordering = ["order"]


class Process(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    steps = models.ManyToManyField(
        "batch.Batch",
        through="batch.Step",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Processes"


class Batch(models.Model):
    description = models.TextField(
        blank=True,
    )
    batch_id = models.CharField(max_length=50, blank=True, unique=True)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.DO_NOTHING,
        related_name="batch",
    )
    cost = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    volume_amount = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True
    )
    volume_unit = models.ForeignKey(
        VolumeUnit,
        on_delete=models.DO_NOTHING,
        related_name="batch",
    )
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Batches"

    def __str__(self):
        return self.batch_id

    def save(self, *args, **kwargs):
        if not self.batch_id:
            self.createdAt = timezone.localtime(timezone.now())
            self.batch_id = "{}-{}:{}".format(
                id_generator(),
                self.createdAt.strftime("%m%d%y"),
                self.createdAt.strftime("%M%S"),
            )
            success = False
            errors = 0
            while not success:
                try:
                    super().save(*args, **kwargs)
                except IntegrityError:
                    errors += 1
                    if errors > 3:
                        # tried 3 times, no dice. raise the integrity error and handle elsewhere
                        raise
                    else:
                        self.batch_id = "{}-{}:{}".format(
                            id_generator(),
                            self.createdAt.strftime("%m%d%y"),
                            self.createdAt.strftime("%M%S"),
                        )
                else:
                    success = True
        else:
            super().save(*args, **kwargs)
