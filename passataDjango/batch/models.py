from django.db import models


class Chef(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


class Variety(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


class Food(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


class VolumeUnit(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    unit = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


class WeightUnit(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    unit = models.CharField(max_length=300, blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)


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


class Step(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
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
    createdAt = models.DateTimeField(auto_now_add=True)


class Batch(models.Model):
    description = models.TextField(
        blank=True,
    )
    batch_id = models.CharField(max_length=50, blank=True, null=True)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.DO_NOTHING,
        related_name="batch",
    )
    variety = models.ForeignKey(
        Variety,
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
    steps = models.ManyToManyField(Step)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.batch_id
