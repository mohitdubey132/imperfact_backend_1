# Generated by Django 4.2.5 on 2023-11-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0013_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='questions',
            name='viewsNo',
            field=models.IntegerField(default=0),
        ),
    ]
