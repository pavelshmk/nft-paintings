# Generated by Django 3.2.4 on 2021-06-22 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_squashed_0004_auto_20210602_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tokendata',
            options={'ordering': ('pk',)},
        ),
    ]