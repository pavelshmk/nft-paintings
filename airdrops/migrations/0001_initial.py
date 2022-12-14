# Generated by Django 3.2.4 on 2021-06-22 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airdrop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveBigIntegerField()),
                ('tokens', models.DecimalField(decimal_places=18, max_digits=64)),
                ('address', models.CharField(max_length=64)),
                ('datetime', models.DateTimeField()),
                ('processed', models.BooleanField(default=False)),
                ('txid', models.CharField(blank=True, max_length=66, null=True)),
            ],
        ),
    ]
