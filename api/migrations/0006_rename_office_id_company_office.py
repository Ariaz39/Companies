# Generated by Django 4.0.3 on 2022-04-26 22:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_company_office_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='office_id',
            new_name='office',
        ),
    ]
