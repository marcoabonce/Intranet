# Generated by Django 3.1 on 2020-10-28 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201021_0206'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Custom',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
