# Generated by Django 4.2.3 on 2023-11-19 12:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_tracetomill'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracetoplantation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mill_eq_id', models.CharField(help_text='mill_eq_id', max_length=255, null=True, verbose_name='mill_eq_id')),
                ('mill_uml_id', models.CharField(help_text='mill_uml_id', max_length=255, null=True, verbose_name='mill_uml_id')),
                ('mill_name', models.CharField(help_text='mill_name', max_length=255, null=True, verbose_name='mill_name')),
                ('agriplot_eq_id', models.CharField(help_text='agriplot_eq_id', max_length=255, null=True, verbose_name='agriplot_eq_id')),
                ('agriplot_type', models.CharField(help_text='agriplot_type', max_length=255, null=True, verbose_name='agriplot_type')),
                ('agriplot_estate_name_id', models.CharField(help_text='agriplot_estate_name_id', max_length=255, null=True, verbose_name='agriplot_estate_name_id')),
                ('agriplot_estate_name', models.CharField(help_text='agriplot_estate_name', max_length=255, null=True, verbose_name='agriplot_estate_name')),
                ('ttp_source_type', models.CharField(help_text='ttp_source_type', max_length=255, null=True, verbose_name='ttp_source_type')),
                ('ttp_year_period', models.CharField(help_text='ttp_year_period', max_length=255, null=True, verbose_name='ttp_year_period')),
                ('ttp_date_update', models.CharField(help_text='ttp_date_update', max_length=255, null=True, verbose_name='ttp_date_update')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Creation date', verbose_name='Created at')),
                ('is_display', models.BooleanField(default=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Tracetoplantation',
                'verbose_name_plural': 'Tracetoplantations',
            },
        ),
    ]
