# Generated by Django 4.2.3 on 2023-08-16 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sandr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_model',
            name='dis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sandr.tags'),
        ),
    ]