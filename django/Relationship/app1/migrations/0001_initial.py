# Generated by Django 3.2.6 on 2021-08-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rtable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('designation', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shivani', models.CharField(max_length=54)),
            ],
        ),
    ]
