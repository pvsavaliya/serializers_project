# Generated by Django 4.0.2 on 2022-03-22 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='isDeleted',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
