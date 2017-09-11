from django.db import models


class AddressBook(models.Model):
    """
    List of addresses
    """
    is_default = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)


class Address(models.Model):
    """
    Address record for a single address
    """
    street = models.CharField(max_length=50, blank=False)
    house_no = models.CharField(max_length=10, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80, blank=True)
    country = models.CharField(max_length=2)
    address_book = models.ForeignKey('AddressBook', null=True, related_name='addresses')