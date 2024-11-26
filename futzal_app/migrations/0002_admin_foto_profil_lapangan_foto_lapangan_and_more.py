# Generated by Django 5.1.3 on 2024-11-26 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futzal_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='foto_profil',
            field=models.ImageField(blank=True, null=True, upload_to='profile/admin/'),
        ),
        migrations.AddField(
            model_name='lapangan',
            name='foto_lapangan',
            field=models.ImageField(blank=True, null=True, upload_to='lapangan/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='foto_profil',
            field=models.ImageField(blank=True, null=True, upload_to='profile/user/'),
        ),
        migrations.AddField(
            model_name='staff',
            name='foto_profil',
            field=models.ImageField(blank=True, null=True, upload_to='profile/staff/'),
        ),
    ]
