# Generated by Django 3.2.21 on 2023-10-31 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_item_offer_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]