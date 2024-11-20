# Generated by Django 5.0.2 on 2024-11-12 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_adopt_pet_adopt_age_adopt_breed_adopt_dogname'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pet',
            name='image',
            field=models.ImageField(default=1, upload_to='dog_image/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trainer_reg',
            name='certificate',
            field=models.FileField(default=1, upload_to='certificate/'),
            preserve_default=False,
        ),
    ]
