# Generated by Django 3.2 on 2021-05-01 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breadcat', '0003_alter_content_sandwich_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='sandwich_id',
        ),
    ]
