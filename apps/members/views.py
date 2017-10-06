from django.shortcuts import render
from django.forms import ChoiceField
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import DetailView, FormView, TemplateView, ListView

from apps.address.models import Address, AddressBook
from apps.main.mixin import LoggedProfileMixin

from .models import Member, MemberStatus
from .forms import NewMemberForm


class SuccessView(TemplateView):
    """
    View for successful member operations
    """
    template_name = 'member/membersuccess.html'


class MemberCreate(FormView, LoggedProfileMixin):
    """
    View for creating a complex form of member/address
    """
    form_class = NewMemberForm
    template_name = 'members/newmember.html'
    member = {}

    def get_initial(self):
        """
        Default values for the member
        """
        initial = super(MemberCreate, self).get_initial()

        # Prepopulate member's status
        statuses = MemberStatus.objects.filter(initial_status=True)
        initial['status'] = ChoiceField(choices=statuses)
        initial['profile'] = self.get_logged_profile()

        return initial

    def get_success_url(self):
        """
        Success URL, based on success created data
        """
        context.email = self.member.email
        context.member_no = self.member_no

        return reverse('member:success', context)

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
            country=form.country,
            address_book=book
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
        self.member = member

        if form.generate_use:
            user = User.objects.create_user(
                username=form.member_no,
                first_name=form.name,
                last_name=form.surname,
                email=form.email,
                password="init1234"
            )


class MemberDetail(DetailView):
    """
    View for displaying a member
    """
    template_name = 'members/memberdetail.html'
    model = Member


class MemberList(ListView):
    """
    View to list all members
    """
    model = Member
    template_name = 'members/memberlist.html'
