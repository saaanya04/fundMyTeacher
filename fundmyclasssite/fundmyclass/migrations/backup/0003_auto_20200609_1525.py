# Generated by Django 3.0.5 on 2020-06-09 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fundmyclass', '0002_auto_20200609_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinfo',
            name='supply_cost',
            field=models.FloatField(default=None),
        ),
    ]
