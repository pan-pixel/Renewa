# Generated by Django 4.2.1 on 2023-05-20 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_alter_blogmodel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/slider/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
