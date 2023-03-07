# Generated by Django 3.2.16 on 2023-01-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('current', models.FloatField()),
                ('voltage', models.FloatField()),
                ('status', models.CharField(max_length=255)),
                ('horometer', models.FloatField()),
            ],
        ),
    ]