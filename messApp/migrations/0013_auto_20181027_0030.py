# Generated by Django 2.1.2 on 2018-10-26 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messApp', '0012_auto_20181027_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
    ]
