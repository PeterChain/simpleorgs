from django.shortcuts import render
from django.forms import ChoiceField
from django.contrib.auth.models import User
from django.views.generic import DetailView, FormView

from apps.address.models import Address, AddressBook

from .models import Member, MemberStatus
from .forms import NewMemberForm


class MemberCreate(FormView):
    """
    View for creating a complex form of member/address
    """
    form_class = NewMemberForm
    template_name = 'members/newmember.html'
    success_url = '/'

    def get_initial(self):
        """
        Default values for the member
        """
        initial = super(MemberCreate, self).get_initial()

        # Prepopulate member's status
        statuses = MemberStatus.objects.filter(initial_status=True)
        statuses_choices = []
        for status in statuses:
            statuses_choices.append(
                (status.status_code, status.status_text)
            )
        initial['status'] = ChoiceField(choices=statuses)

        return initial

    def form_valid(self, form):
        """
        Form submited successfully
        """

        #1st step - Create an address book with default address
        book = AddressBook.objects.create(
            is_default=True,
            is_active=True
        )

        # 2nd step - Create the address
        address = Address.objects.create(
            street=form.street,
            house_no=form.street,
            postal_code=form.postal_code,
            city=form.city,
            state=form.state,
            country=form.country
            addresses=book
        )

        # 3rd step - The member and user (when applied)
        member = Member.objects.create(
            name=form.name,
            surname=form.surname,
            date_of_birth=form.date_of_birth,
            email=form.email,
            telephone=form.telephone,
            status=form.status,
            picture=form.picture,
            nationality=form.nationality,
            address_book=book
        )

        if form.generate_use:
            user = User.objects.create_user(
                username=form.member_no,
                email=form.email,
                password="init1234"
            ) 


class MemberDetail(DetailView):
    """
    View for displaying a member
    """
    template_name = 'members/memberdetail.html'
    model = Member
