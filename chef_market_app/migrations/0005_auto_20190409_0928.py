# Generated by Django 2.1.7 on 2019-04-09 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chef_market_app', '0004_auto_20190408_1110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderingredient',
            name='ingredient',
        ),
        migrations.RemoveField(
            model_name='orderingredient',
            name='order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ingredients',
        ),
        migrations.AddField(
            model_name='order',
            name='dish',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='chef_market_app.Dish'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=9),
        ),
        migrations.DeleteModel(
            name='OrderIngredient',
        ),
    ]