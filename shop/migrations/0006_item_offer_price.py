# Generated by Django 3.2.21 on 2023-10-31 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_item_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='offer_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]