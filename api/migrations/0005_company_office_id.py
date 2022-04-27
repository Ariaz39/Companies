# Generated by Django 4.0.3 on 2022-04-26 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_offices_alter_company_options_alter_company_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='office_id',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='api.offices'),
            preserve_default=False,
        ),
    ]
