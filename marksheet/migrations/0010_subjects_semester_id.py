# Generated by Django 5.2.1 on 2025-06-17 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marksheet', '0009_studentprofile_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='semester_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='marksheet.semester'),
        ),
    ]
