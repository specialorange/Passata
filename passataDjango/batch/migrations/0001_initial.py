# Generated by Django 3.1.8 on 2022-06-18 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='VolumeUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('unit', models.CharField(blank=True, max_length=300, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeightUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('unit', models.CharField(blank=True, max_length=300, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('initial_weight_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('final_weight_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('order', models.CharField(blank=True, max_length=10, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('chefs', models.ManyToManyField(to='batch.Chef')),
                ('weight_unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='step', to='batch.weightunit')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
                ('volume_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ingredient', to='batch.food')),
                ('volume_unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ingredient', to='batch.volumeunit')),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('batch_id', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('volume_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='batch', to='batch.ingredient')),
                ('steps', models.ManyToManyField(to='batch.Step')),
                ('variety', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='batch', to='batch.variety')),
                ('volume_unit', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='batch', to='batch.volumeunit')),
            ],
        ),
    ]
