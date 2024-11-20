# Generated by Django 5.1.1 on 2024-10-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phno', models.IntegerField()),
                ('password', models.CharField(max_length=50)),
                ('confirmPassword', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
    ]