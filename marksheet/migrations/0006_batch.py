# Generated by Django 5.2.1 on 2025-06-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marksheet', '0005_semester_alter_user_first_name_alter_user_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heads', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'BATCH SETUP',
                'db_table': 't_batch',
            },
        ),
    ]
