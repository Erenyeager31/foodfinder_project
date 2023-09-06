# Generated by Django 4.2 on 2023-08-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder_app', '0005_rename__ifsc_seller_details_ifsc'),
    ]

    operations = [
        migrations.CreateModel(
            name='food_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('food_name', models.CharField(max_length=25)),
                ('food_cat', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
                ('img_url', models.CharField(max_length=100)),
            ],
        ),
    ]