# Generated by Django 4.0.3 on 2022-04-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_company_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Office',
                'verbose_name_plural': 'Offices',
                'db_table': 'api_office',
            },
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Company', 'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelTable(
            name='company',
            table='api_companies',
        ),
    ]
