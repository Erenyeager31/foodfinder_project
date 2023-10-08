# Generated by Django 4.2 on 2023-10-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder_app', '0011_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=30)),
                ('rating', models.CharField(max_length=10)),
                ('review', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=10)),
            ],
        ),
    ]