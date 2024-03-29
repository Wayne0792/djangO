# Generated by Django 4.2.3 on 2023-07-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=25)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=250)),
                ('city', models.CharField(max_length=12)),
                ('provincee', models.CharField(max_length=12)),
            ],
        ),
    ]
