from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField( max_length =250 )
    snippet = models.TextField(
        blank = True,
        null = True,
    )
    cost = models.DecimalField(
        max_digits = 12,
        decimal_places = 2,
        default = 0,
    )
    modified = models.DateTimeField(
        auto_now = True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
