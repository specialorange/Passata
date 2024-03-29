# Generated by Django 4.0.5 on 2022-06-23 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0009_remove_batch_steps_remove_process_batch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='steps',
            field=models.ManyToManyField(null=True, through='batch.Step', to='batch.batch'),
        ),
        migrations.AddField(
            model_name='step',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='step', to='batch.batch'),
        ),
        migrations.AddField(
            model_name='step',
            name='process',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='step', to='batch.process'),
        ),
    ]
