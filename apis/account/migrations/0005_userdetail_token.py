# Generated by Django 4.0.2 on 2022-03-14 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_emailotp'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='Token',
            field=models.TextField(null=True),
        ),
    ]
