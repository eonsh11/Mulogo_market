# Generated by Django 4.0.1 on 2022-01-25 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_postcomment'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='postcomment',
            table='comment1',
        ),
    ]