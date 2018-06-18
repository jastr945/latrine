# Generated by Django 2.0.3 on 2018-06-02 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latrineapp', '0004_auto_20180531_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.TextField(default='', max_length=255),
        ),
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
        migrations.AlterField(
            model_name='place',
            name='phone',
            field=models.TextField(default='', max_length=255, null=True),
        ),
    ]
