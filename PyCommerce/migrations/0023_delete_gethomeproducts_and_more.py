# Generated by Django 4.2.4 on 2023-08-13 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0022_alter_categories_maincategoryid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='getHomeProducts',
        ),
        migrations.DeleteModel(
            name='specificationValueCount',
        ),
        migrations.DeleteModel(
            name='starPercent',
        ),
    ]