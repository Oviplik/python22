# Generated by Django 4.2.6 on 2023-11-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_feedback_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telebot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=16, unique=True)),
                ('user_name', models.CharField(max_length=16, unique=True)),
                ('user_sname', models.CharField(max_length=16, unique=True)),
                ('user_time', models.CharField(max_length=16)),
            ],
        ),
    ]
