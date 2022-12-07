from django.db import models


class TokenData(models.Model):
    title = models.CharField(default='', max_length=128)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = 'pk',
