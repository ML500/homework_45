# Generated by Django 2.2 on 2020-07-28 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20200725_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='detail',
            field=models.TextField(blank=True, default='no description', max_length=3000, null=True, verbose_name='Detail'),
        ),
    ]
