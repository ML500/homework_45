# Generated by Django 2.2 on 2020-07-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200722_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='execute_at',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Date of execution'),
        ),
    ]
