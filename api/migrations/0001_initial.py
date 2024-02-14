# Generated by Django 4.2.10 on 2024-02-14 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('customer_xid', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=255)),
                ('created_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_xid', models.CharField(max_length=255)),
                ('transaction_datetime', models.DateTimeField()),
                ('status', models.CharField(max_length=255)),
                ('reference_id', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owned_by', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('enabled_at', models.DateTimeField()),
                ('disabled_at', models.DateTimeField()),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]