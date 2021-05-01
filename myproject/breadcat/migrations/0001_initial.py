# Generated by Django 3.2 on 2021-05-01 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField(default='')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ingredient', models.CharField(choices=[('vegetables', 'vegetable'), ('tomato', 'tomato'), ('cheese', 'cheese'), ('bacon', 'bacon')], default='bacon', max_length=15)),
            ],
        ),
    ]