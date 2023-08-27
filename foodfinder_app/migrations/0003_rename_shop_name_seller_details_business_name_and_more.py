# Generated by Django 4.2 on 2023-08-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodfinder_app', '0002_user_detail_seller_details_shop_add_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller_details',
            old_name='shop_name',
            new_name='business_name',
        ),
        migrations.AddField(
            model_name='seller_details',
            name='bank_act_no',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='seller_details',
            name='branch_name',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='seller_details',
            name='city',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='seller_details',
            name='state',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='seller_details',
            name='zip',
            field=models.CharField(default='', max_length=6),
        ),
    ]
