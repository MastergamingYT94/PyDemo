# Generated by Django 3.2.4 on 2021-06-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0003_auto_20210617_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermasters',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='orders',
            name='id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
