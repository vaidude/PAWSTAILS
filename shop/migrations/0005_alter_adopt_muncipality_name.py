# Generated by Django 5.0.2 on 2024-11-06 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_remove_adopt_muncipality_adopt_muncipality_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adopt',
            name='muncipality_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adopt', to='shop.muncipality'),
        ),
    ]
