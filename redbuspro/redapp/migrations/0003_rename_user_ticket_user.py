# Generated by Django 3.2.6 on 2021-08-07 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redapp', '0002_alter_user_password'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Ticket_User',
        ),
    ]
