# Generated by Django 4.0.5 on 2022-06-20 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0004_remove_batch_ingredient_recipe_batch_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]