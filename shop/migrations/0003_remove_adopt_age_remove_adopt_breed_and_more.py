# Generated by Django 5.0.2 on 2024-11-06 06:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_adopt_donation_amount_muncipality_pay_pet_timetable_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopt',
            name='age',
        ),
        migrations.RemoveField(
            model_name='adopt',
            name='breed',
        ),
        migrations.RemoveField(
            model_name='adopt',
            name='dogname',
        ),
        migrations.AddField(
            model_name='adopt',
            name='pet',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='adopt', to='shop.pet'),
            preserve_default=False,
        ),
    ]
