# Generated by Django 3.1.1 on 2020-09-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200911_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='portrait',
            field=models.ImageField(default='default.png', upload_to='photo'),
        ),
    ]
