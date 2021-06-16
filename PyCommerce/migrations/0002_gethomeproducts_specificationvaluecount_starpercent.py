# Generated by Django 3.2.4 on 2021-06-16 16:09

from django.db import migrations, models
import django_resized.forms


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
                ('ProductName', models.TextField(max_length=2550)),
                ('StoreName', models.TextField(max_length=2550)),
                ('Image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='')),
                ('Image2', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='')),
                ('Image3', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='')),
                ('Image4', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='')),
                ('Description', models.TextField(max_length=2550)),
                ('Price', models.FloatField()),
                ('Currency', models.TextField(max_length=2550)),
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
                'db_table': 'gethomeproducts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='specificationValueCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SpecificationId', models.IntegerField()),
                ('SpecificationValue', models.TextField(max_length=2550)),
                ('SpecificationCount', models.IntegerField()),
                ('CategoryId', models.IntegerField()),
            ],
            options={
                'db_table': 'specificationvaluecount',
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
                'db_table': 'getstarpercent',
                'managed': False,
            },
        ),
    ]
