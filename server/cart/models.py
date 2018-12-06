import json
from django.db import models
from functools import reduce
from django.apps import apps
from django.core.exceptions import ValidationError

class Purchase(models.Model):
    user = models.ForeignKey(
        #'auth.User',
        'accounts.AccountUser',
        on_delete = models.CASCADE,
    )
    created = models.DateTimeField(
        auto_now_add = True
    )

    @property
    def cost(self):
        return reduce(
            lambda total, itm: total + itm.product.cost,
            self.items.all(),
            0
        )

    @property
    def count(self):
        return reduce(
            lambda total, itm: total + itm.value,
            self.items.all(),
            0
        )

    def __str__(self):
        full_name = self.user.get_full_name()
        title = full_name if full_name else self.user.username
        return f'{title} {self.created.strftime("%Y-%m-%d %H:%M")}'

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(
        Purchase,
        on_delete = models.CASCADE,
        related_name = 'items',
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete = models.CASCADE
    )
    value = models.IntegerField()

    def __str__(self):
        return self.product.title
