# Generated by Django 5.0.6 on 2024-06-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProntaEntregaApp', '0013_alter_usuario_is_superuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios/'),
        ),
    ]