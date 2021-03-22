# Generated by Django 3.1.6 on 2021-03-22 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill_Setting',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('StoreName', models.TextField()),
                ('VAT', models.IntegerField()),
                ('SC', models.IntegerField()),
                ('EndTextBill', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('User', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('Lastname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('jobposition', models.CharField(max_length=255)),
                ('ID_card', models.CharField(max_length=50)),
                ('ID_job', models.CharField(max_length=50)),
                ('ID_bank', models.CharField(max_length=50)),
                ('Bank', models.CharField(max_length=255)),
                ('Salary', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('foodname', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=255)),
                ('status_menu', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Order_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('type_order', models.TextField(max_length=255)),
                ('number_table', models.TextField(max_length=255)),
                ('name', models.TextField(max_length=255)),
                ('status_order', models.TextField(max_length=100)),
                ('total', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Owners',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('Lastname', models.CharField(max_length=255)),
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
            name='Q',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Order_id', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=3)),
                ('Quantity', models.CharField(max_length=5)),
                ('Order_id', models.TextField(max_length=255)),
                ('status_table', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('time_day', models.CharField(max_length=255)),
                ('tip_cash', models.IntegerField()),
                ('tip_tran', models.IntegerField()),
                ('tip_total', models.IntegerField()),
                ('Order_id', models.ForeignKey(blank=True, db_column='Order_id', on_delete=django.db.models.deletion.DO_NOTHING, to='projectpos.order')),
            ],
        ),
        migrations.CreateModel(
            name='receipt',
            fields=[
                ('ID', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Order_id', models.ForeignKey(blank=True, db_column='Order_id', on_delete=django.db.models.deletion.DO_NOTHING, to='projectpos.order')),
            ],
        ),
        migrations.CreateModel(
            name='Orderlish',
            fields=[
                ('Orderlish_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nume_food', models.TextField(max_length=255)),
                ('price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('category', models.TextField(max_length=255)),
                ('status', models.TextField(max_length=255)),
                ('Order_id', models.ForeignKey(blank=True, db_column='Order_id', on_delete=django.db.models.deletion.DO_NOTHING, to='projectpos.order')),
            ],
        ),
    ]
