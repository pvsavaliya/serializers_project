# Generated by Django 4.0.2 on 2022-03-04 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='media',
            field=models.FileField(blank=True, null=True, upload_to='message/%Y/%m/%d/'),
        ),
    ]