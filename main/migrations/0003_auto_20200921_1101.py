# Generated by Django 3.1 on 2020-09-21 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200921_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classifiedtype',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='labeledimage',
            old_name='user_id',
            new_name='user',
        ),
    ]
