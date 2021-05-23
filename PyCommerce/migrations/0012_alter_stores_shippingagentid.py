# Generated by Django 3.2.3 on 2021-05-20 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0011_alter_stores_shippingagentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stores',
            name='ShippingAgentId',
            field=models.ForeignKey(db_column='ShippingAgentId', on_delete=django.db.models.deletion.DO_NOTHING, related_name='entries', to='PyCommerce.shippingagents', verbose_name='NameL'),
        ),
    ]
