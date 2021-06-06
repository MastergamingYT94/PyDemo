# Generated by Django 3.2.3 on 2021-05-30 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PyCommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='getHomeProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuantityBalance', models.FloatField()),
                ('ProductName', models.CharField(max_length=2550)),
                ('StoreName', models.CharField(max_length=2550)),
                ('ImageUrl', models.CharField(max_length=2550)),
                ('ImageUrl6', models.CharField(max_length=2550)),
                ('ImageUrl7', models.CharField(max_length=2550)),
                ('Description', models.CharField(max_length=2550)),
                ('Price', models.FloatField()),
                ('Currency', models.CharField(max_length=2550)),
                ('PageNumber', models.IntegerField()),
                ('FiveStarsCount', models.FloatField()),
                ('FourStarsCount', models.FloatField()),
                ('ThreeStarsCount', models.FloatField()),
                ('TwoStarsCount', models.FloatField()),
                ('OneStarsCount', models.FloatField()),
                ('MaxTotalRating', models.FloatField()),
                ('finalProductRating', models.FloatField()),
                ('OutOfFivestring', models.FloatField()),
            ],
            options={
                'db_table': 'GetHomeProducts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='specificationValueCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpecificationId', models.IntegerField()),
                ('SpecificationValue', models.CharField(max_length=2550)),
                ('SpecificationCount', models.IntegerField()),
                ('CategoryId', models.IntegerField()),
            ],
            options={
                'db_table': 'SpecificationValueCount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='starPercent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FiveStarsCount', models.FloatField()),
                ('FourStarsCount', models.FloatField()),
                ('ThreeStarsCount', models.FloatField()),
                ('TwoStarsCount', models.FloatField()),
                ('OneStarCount', models.FloatField()),
                ('FiveStarsPercent', models.FloatField()),
                ('FourStarsPercent', models.FloatField()),
                ('ThreeStarsPercent', models.FloatField()),
                ('TwoStarsPercent', models.FloatField()),
                ('OneStarPercent', models.FloatField()),
                ('averageRating', models.FloatField()),
                ('OutOfFive', models.FloatField()),
                ('allReviewsCount', models.IntegerField()),
            ],
            options={
                'db_table': 'GetStarPercent',
                'managed': False,
            },
        ),
    ]
