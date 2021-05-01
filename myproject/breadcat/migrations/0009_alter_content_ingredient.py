# Generated by Django 3.2 on 2021-05-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breadcat', '0008_delete_sandwich'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='ingredient',
            field=models.CharField(choices=[('basil', 'basil'), ('tomato', 'tomato'), ('cheese', 'cheese'), ('bacon', 'bacon')], default='bacon', max_length=15),
        ),
    ]
