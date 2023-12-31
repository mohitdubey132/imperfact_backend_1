# Generated by Django 4.2.5 on 2023-12-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0018_answers'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='dis_liked_by',
            field=models.ManyToManyField(related_name='dis_liked_questions', to='restAPI.customuser'),
        ),
        migrations.AddField(
            model_name='question',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_questions', to='restAPI.customuser'),
        ),
    ]
