# Generated by Django 4.2.5 on 2023-11-26 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0009_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='userName',
        ),
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
