# Generated by Django 4.2 on 2023-09-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder_app', '0009_seller_details_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='business_location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('business_name', models.CharField(default='', max_length=20)),
                ('location', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
