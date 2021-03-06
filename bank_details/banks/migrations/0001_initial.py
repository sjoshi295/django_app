# Generated by Django 2.2.4 on 2019-08-26 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankName',
            fields=[
                ('bank_name', models.CharField(max_length=200, unique=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='BankData',
            fields=[
                ('ifsc', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('branch', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='b_id', to='banks.BankName')),
            ],
            options={
                'ordering': ['ifsc'],
            },
        ),
    ]
