# Generated by Django 3.1.6 on 2021-03-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectpos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owners',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='table',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
