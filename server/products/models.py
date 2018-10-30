from django.db import models


class Category(models.Model):
    title = models.CharField( max_length =250 )

    snippet = models.TextField(
        blank = True,
        null = True,
    )

    modified = models.DateTimeField(
        auto_now = True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )



class Product(models.Model):
    title = models.CharField( max_length =250 )


    category = models.ForeignKey(
        Category,
        on_delete = models.CASCADE
    )
    image = models.ImageField(
        upload_to = 'products'
    )

    snippet = models.TextField(
        blank=True,
        null=True,
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
