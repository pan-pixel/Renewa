# Generated by Django 4.2.1 on 2023-05-21 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_grocery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_type', models.TextField(max_length=255)),
                ('address', models.TextField(max_length=255)),
            ],
        ),
    ]
