# Generated by Django 4.2.3 on 2023-11-19 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_refinery'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='facilities_name',
            field=models.CharField(help_text='facilities_name', max_length=255, null=True, verbose_name='facilities_name'),
        ),
        migrations.AddField(
            model_name='refinery',
            name='refinery_name',
            field=models.CharField(help_text='refinery_name', max_length=255, null=True, verbose_name='refinery_name'),
        ),
    ]