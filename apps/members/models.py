from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_countries.fields import CountryField

from apps.address.models import AddressBook


class MemberStatus(models.Model):
    """
    Member's possible status
    """
    STATUS_TYPE = (
        ('V', _('Valid')),
        ('I', _('Intermediary')),
        ('F', _('Final'))
    )

    status_code = models.CharField(max_length=3)
    status_text = models.CharField(max_length=80)
    initial_status = models.BooleanField(default=True)
    status_type = models.CharField(max_length=1, 
                                   choices=STATUS_TYPE, 
                                   default='V')


class Member(models.Model):
    """
    Member of the organization
    """
    member_no = models.CharField(max_length=5, blank=True, unique=True)
    name = models.CharField(max_length=80, blank=False)
    surname = models.CharField(max_length=80, blank=False)
    nationality = CountryField()
    date_of_birth = models.DateField(auto_now=False, blank=True)
    email = models.CharField(max_length=120, blank=False)
    telephone = models.CharField(max_length=20, blank=True)
    slug = models.CharField(max_length=6, blank=True)
    address_book = models.OneToOneField('address.AddressBook', 
                                        related_name='address_book', 
                                        on_delete=models.CASCADE,
                                        null=True)
    status = models.CharField(max_length=3, null=True, blank=True)
    picture = models.ImageField(upload_to='profiles')

    def __str__(self):
        return self.member_no
    
    def slug(self):
        return self.member_no


class MemberEmploymentHistory(models.Model):
    """
    Member's professional records
    """
    date_from = models.DateField(auto_now=False, blank=True)
    date_to = models.DateField(auto_now=True, blank=True)
    title = models.CharField(max_length=255)
    workplace = models.CharField(max_length=255)
    current = models.BooleanField(default=True)

