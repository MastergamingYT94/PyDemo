# Generated by Django 3.2.5 on 2021-08-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0015_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='Image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]