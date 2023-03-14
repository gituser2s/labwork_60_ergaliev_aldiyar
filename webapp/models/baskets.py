from django.db import models


class Basket(models.Model):
    count = models.IntegerField(
        verbose_name="Остаток",
        null=False,
        blank=False
    )
    product = models.ForeignKey(
        to='webapp.Product',
        on_delete=models.PROTECT,
        related_name="product"
    )



