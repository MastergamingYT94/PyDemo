# Generated by Django 3.2.3 on 2021-05-20 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0004_auto_20210520_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carttransactions',
            name='MasterId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carttransactions',
            name='ProductId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='carttransactions',
            name='StoreId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordermasters',
            name='OrderStatusId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ordermasters',
            name='UserId',
            field=models.IntegerField(),
        ),
    ]
