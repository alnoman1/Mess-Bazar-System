# Generated by Django 2.1.2 on 2018-10-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.PositiveIntegerField(blank=True, null=True)),
                ('timestimp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
