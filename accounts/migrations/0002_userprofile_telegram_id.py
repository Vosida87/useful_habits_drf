# Generated by Django 4.2.5 on 2023-09-30 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='telegram_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Telegram id'),
        ),
    ]
