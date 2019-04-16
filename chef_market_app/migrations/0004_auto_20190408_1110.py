# Generated by Django 2.1.7 on 2019-04-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef_market_app', '0003_ingredient_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
    ]