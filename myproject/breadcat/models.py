from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class Content(models.Model):
    ingredient_choices = (
        ('basil', 'basil'),
        ('tomato', 'tomato'),
        ('cheese', 'cheese'),
        ('bacon', 'bacon'),
    )
    question = models.CharField(max_length=200)
    answer = models.TextField(default='')
    date = models.DateTimeField(default=timezone.now)
    ingredient = models.CharField(
        max_length=15,
        choices=ingredient_choices,
        default='bacon',
    )
