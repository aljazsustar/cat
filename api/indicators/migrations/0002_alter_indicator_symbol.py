# Generated by Django 4.1.1 on 2022-09-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='symbol',
            field=models.CharField(max_length=50),
        ),
    ]
