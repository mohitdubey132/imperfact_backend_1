# Generated by Django 4.2.5 on 2023-11-26 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0011_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='email',
        ),
        migrations.AddField(
            model_name='customuser',
            name='userName',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='mobileNo',
            field=models.CharField(max_length=10),
        ),
    ]
