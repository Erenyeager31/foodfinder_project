# Generated by Django 4.2 on 2023-08-27 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder_app', '0004_seller_details__ifsc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_details',
            old_name='_ifsc',
            new_name='ifsc',
        ),
    ]
