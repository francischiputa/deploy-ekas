# Generated by Django 4.0.6 on 2022-07-07 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Ekas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='date_time_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
