# Generated by Django 3.2.21 on 2023-10-30 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20231030_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='N', max_length=1),
            preserve_default=False,
        ),
    ]