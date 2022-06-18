from django.contrib import admin
from batch import models


@admin.register(models.Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(models.Variety)
class VarietyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(models.Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(models.VolumeUnit)
class VolumeUnitAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "unit",
    ]


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "food",
        "volume_amount",
        "volume_unit",
    ]


@admin.register(models.Step)
class StepAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "initial_weight_amount",
        "final_weight_amount",
        "weight_unit",
        "order",
        "start_time",
        "end_time",
    ]


@admin.register(models.Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = [
        "description",
        "batch_id",
        "ingredient",
        "variety",
        "cost",
        "volume_amount",
        "volume_unit",
        "start_time",
        "end_time",
    ]
