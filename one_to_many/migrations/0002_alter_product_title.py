# Generated by Django 5.1.4 on 2024-12-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one_to_many', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
