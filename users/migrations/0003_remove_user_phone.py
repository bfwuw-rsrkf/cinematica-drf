# Generated by Django 4.2.5 on 2023-09-25 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_discountcard_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]