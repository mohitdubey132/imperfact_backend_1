# Generated by Django 4.2.5 on 2023-12-06 17:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restAPI', '0015_delete_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('dislike_count', models.PositiveIntegerField(default=0)),
                ('Q_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restAPI.customuser')),
            ],
        ),
    ]
