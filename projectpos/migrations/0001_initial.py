# Generated by Django 3.1.6 on 2021-03-07 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=255)),
                ('ID_card', models.CharField(max_length=13)),
                ('ID_job', models.CharField(max_length=5)),
                ('store_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=3)),
                ('people', models.CharField(max_length=2)),
                ('time', models.CharField(max_length=10)),
                ('order', models.CharField(max_length=255)),
            ],
        ),
    ]
