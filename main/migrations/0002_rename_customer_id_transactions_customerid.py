# Generated by Django 3.2.4 on 2021-07-09 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transactions',
            old_name='Customer_ID',
            new_name='CustomerID',
        ),
    ]