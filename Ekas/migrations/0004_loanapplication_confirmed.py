# Generated by Django 4.0.6 on 2022-07-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ekas', '0003_alter_loanapplication_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Tick the checkbox if Application has been Approved.'),
        ),
    ]
