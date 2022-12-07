from django.db import models


class Airdrop(models.Model):
    user_id = models.PositiveBigIntegerField()
    tokens = models.DecimalField(max_digits=64, decimal_places=18)
    address = models.CharField(max_length=64)
    datetime = models.DateTimeField()
    processed = models.BooleanField(default=False)
    txid = models.CharField(max_length=66, null=True, blank=True)
