# Generated by Django 3.1.3 on 2020-11-17 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20201117_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='companies',
            field=models.ManyToManyField(to='company.Company'),
        ),
    ]