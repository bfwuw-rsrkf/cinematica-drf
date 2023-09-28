# Generated by Django 4.2.5 on 2023-09-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_orders_tickettype_ticket'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='sessions',
            new_name='session',
        ),
        migrations.AddField(
            model_name='ticket',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
