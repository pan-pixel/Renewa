# Generated by Django 4.2.1 on 2023-05-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_blogmodel_image_alter_blogmodel_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='NightFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='media/slider/%Y/%m')),
                ('title', models.TextField(max_length=255)),
                ('price', models.TextField(max_length=255)),
            ],
        ),
    ]
