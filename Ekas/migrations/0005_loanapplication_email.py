# Generated by Django 4.0.6 on 2022-07-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ekas', '0004_loanapplication_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanapplication',
            name='email',
            field=models.EmailField(default='Jack@jacktembo.com', max_length=64),
            preserve_default=False,
        ),
    ]
