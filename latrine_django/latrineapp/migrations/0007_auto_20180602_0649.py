# Generated by Django 2.0.3 on 2018-06-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latrineapp', '0006_auto_20180602_0648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.FloatField(),
        ),
    ]
