# Generated by Django 4.1 on 2022-09-01 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nuguhome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='mapurl',
            field=models.TextField(default=''),
        ),
    ]
