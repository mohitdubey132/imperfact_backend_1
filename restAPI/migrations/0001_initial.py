# Generated by Django 4.2.5 on 2023-11-26 09:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('U_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('userType', models.CharField(max_length=255)),
                ('fullName', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('mobileNo', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=255)),
            ],
        ),
    ]
