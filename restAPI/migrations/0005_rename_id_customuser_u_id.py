# Generated by Django 4.2.5 on 2023-11-26 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0004_rename_u_id_customuser_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='id',
            new_name='U_id',
        ),
    ]
