# Generated by Django 4.2.3 on 2023-11-19 11:02

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_mill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agriplot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ID_Mill', models.CharField(help_text='ID_Mill', max_length=255, null=True, verbose_name='ID_Mill')),
                ('Mill_Name', models.CharField(help_text='Mill_Name', max_length=255, null=True, verbose_name='Mill_Name')),
                ('Ownership', models.CharField(help_text='Ownership', max_length=255, null=True, verbose_name='Ownership')),
                ('Subsidiary', models.CharField(help_text='Subsidiary', max_length=255, null=True, verbose_name='Subsidiary')),
                ('Estate', models.CharField(help_text='Estate', max_length=255, null=True, verbose_name='Estate')),
                ('ID_Estate', models.CharField(help_text='ID_Estate', max_length=255, null=True, verbose_name='ID_Estate')),
                ('AgriplotID', models.CharField(help_text='AgriplotID', max_length=255, null=True, verbose_name='AgriplotID')),
                ('TypeOfSupp', models.CharField(help_text='TypeOfSupp', max_length=255, null=True, verbose_name='TypeOfSupp')),
                ('Village', models.CharField(help_text='Village', max_length=255, null=True, verbose_name='Village')),
                ('SubDistric', models.CharField(help_text='SubDistric', max_length=255, null=True, verbose_name='SubDistric')),
                ('District', models.CharField(help_text='District', max_length=255, null=True, verbose_name='District')),
                ('Province', models.CharField(help_text='Province', max_length=255, null=True, verbose_name='Province')),
                ('Country', models.CharField(help_text='Country', max_length=255, null=True, verbose_name='Country')),
                ('Planted_Ar', models.DecimalField(decimal_places=6, help_text='Planted_Ar', max_digits=9, null=True, verbose_name='Planted_Ar')),
                ('YearUpdate', models.CharField(help_text='YearUpdate', max_length=255, null=True, verbose_name='YearUpdate')),
                ('RiskAssess', models.CharField(help_text='RiskAssess', max_length=255, null=True, verbose_name='RiskAssess')),
                ('GHG_LUC', models.CharField(help_text='GHG_LUC', max_length=255, null=True, verbose_name='GHG_LUC')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date', verbose_name='Created at')),
                ('geom', django.contrib.gis.db.models.fields.PolygonField(blank=True, dim=3, null=True, srid=4326)),
                ('is_display', models.BooleanField(default=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Agriplot',
                'verbose_name_plural': 'Agriplots',
            },
        ),
    ]
