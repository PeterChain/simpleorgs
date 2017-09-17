from django.urls import reverse
from django.views.generic import ListView

from .models import Address


class AddressBookListView(ListView):
    """
    View class the address book
    """
    template_name = 'address/book.html'
    model = Address
