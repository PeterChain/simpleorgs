from django.db import models


from apps.address.models import AddressBook


class MemberStatus(models.Model):
    """
    Member's possible status
    """
    status_code = models.CharField(max_length=3)
    status_text = models.CharField(max_length=80)


class Member(models.Model):
    """
    Member of the organization
    """
    member_no = models.CharField(max_length=5, blank=True, unique=True)
    name = models.CharField(max_length=45, blank=False)
    middle_name = models.CharField(max_length=45, blank=True)
    surname = models.CharField(max_length=45, blank=False)
    date_of_birth = models.DateField(auto_now=False, blank=True)
    email = models.CharField(max_length=120, blank=False)
    telephone = models.CharField(max_length=20, blank=True)
    slug = models.CharField(max_length=6, blank=True)
    address_book = models.OneToOneField('address.AddressBook', 
                                        related_name='address_book', 
                                        on_delete=models.CASCADE,
                                        null=True)
    status = models.CharField(max_length=3, blank=True)
    picture = models.ImageField(upload_to='profiles')


class MemberEmploymentHistory(models.Model):
    """
    Member's professional records
    """
    date_from = models.DateField(auto_now=False, blank=True)
    date_to = models.DateField(auto_now=True, blank=True)
    title = models.CharField(max_length=255)
    workplace = models.CharField(max_length=255)
    current = models.BooleanField(default=True)

