# Generated by Django 4.2.5 on 2023-11-26 10:23

from django.db import migrations, models
import restAPI.models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='userType',
            field=models.CharField(choices=[(restAPI.models.UserType['USER'], 'user'), (restAPI.models.UserType['ADMIN'], 'admin'), (restAPI.models.UserType['EXPERT'], 'expert'), (restAPI.models.UserType['SPECIAL_PERSON'], 'special_person')], max_length=20),
        ),
    ]
