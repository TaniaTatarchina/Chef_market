# Generated by Django 2.1.7 on 2019-04-10 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190402_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(default='1', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(default='1', max_length=32),
            preserve_default=False,
        ),
    ]
