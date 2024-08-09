from django.db import models

class Items(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
