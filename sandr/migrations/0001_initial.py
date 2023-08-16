# Generated by Django 4.2.3 on 2023-08-16 03:52

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products_model',
            fields=[
                ('product_image', models.ImageField(upload_to='product_img/')),
                ('products_name', models.CharField(max_length=200)),
                ('product_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount', models.BooleanField(default=False)),
            ],
        ),
    ]