# Generated by Django 4.2.4 on 2023-08-14 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0026_alter_gethomeproducts_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gethomeproducts',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='specificationvaluecount',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='starpercent',
            options={'managed': False},
        ),
    ]