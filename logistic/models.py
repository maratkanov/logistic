from django.db import models


class SimpleRequestModel(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)

    is_seen = models.BooleanField(default=False)


class RequestModel(models.Model):
    name = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    ship_date = models.DateTimeField()
    from_address = models.CharField(max_length=30, blank=True)
    to_address = models.CharField(max_length=30, blank=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    weight = models.PositiveIntegerField(blank=True, null=True)
    code = models.PositiveIntegerField(blank=True, null=True)
    size = models.PositiveIntegerField(blank=True, null=True)
    places = models.PositiveIntegerField(blank=True, null=True)

    is_seen = models.BooleanField(default=False)
