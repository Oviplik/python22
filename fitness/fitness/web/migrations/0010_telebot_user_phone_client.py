# Generated by Django 4.2.6 on 2023-11-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_telebot_trener_telebot_type_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='telebot',
            name='user_phone_client',
            field=models.CharField(default='', max_length=16),
            preserve_default=False,
        ),
    ]
