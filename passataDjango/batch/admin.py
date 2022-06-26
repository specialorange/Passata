from django.contrib import admin
from batch import models


@admin.register(models.Chef)
class ChefAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


class IngredientInline(admin.TabularInline):
    model = models.Recipe.ingredients.through
    extra = 1


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "food",
        "full_name",
        "volume_amount",
        "volume_unit",
    ]


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "steps",
    ]
    inlines = [IngredientInline]


class StepsInline(admin.TabularInline):
    # class StepsInline(admin.StackedInline):
    model = models.Process.steps.through


@admin.register(models.Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]
    inlines = [StepsInline]


@admin.register(models.Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "phone_number",
        "email",
        "phone_type",
        "country_code",
        "area_code",
        "pnumber",
        "extension",
    ]


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "__str__",
        "name",
        "order_id",
        "createdAt",
        "consumer",
        "fulfilled",
        "delivery",
        "volume_amount",
        "volume_unit",
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


@admin.register(models.WeightUnit)
class WeightUnitAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "unit",
    ]


@admin.register(models.BasicStep)
class BasicStepAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(models.Step)
class StepAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "batch",
        "process",
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
        "batch_id",
        "description",
        "recipe",
        "cost",
        "volume_amount",
        "volume_unit",
        "start_time",
        "end_time",
    ]
