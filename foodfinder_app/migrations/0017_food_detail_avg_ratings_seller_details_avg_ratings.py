# Generated by Django 4.2 on 2023-10-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder_app', '0016_shop_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_detail',
            name='avg_ratings',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='seller_details',
            name='avg_ratings',
            field=models.IntegerField(default=0),
        ),
    ]
