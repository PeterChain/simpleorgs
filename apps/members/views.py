from django.db import transaction
from django.shortcuts import render
from django.forms import ChoiceField
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic import UpdateView, FormView, TemplateView, ListView

from apps.address.models import Address, AddressBook
from apps.main.mixin import UserAuthMixin

from .models import Member, MemberStatus
from .forms import NewMemberForm


class SuccessView(TemplateView):
    """
    View for successful member operations
    """
    template_name = 'members/membersuccess.html'
    model = Member


class MemberCreate(FormView, UserAuthMixin):
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
        data = {}
        data['slug'] = self.member.member_no

        return reverse('members:success', kwargs=data)
    
    @transaction.atomic
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
            street=form.cleaned_data['street'],
            house_no=form.cleaned_data['street'],
            postal_code=form.cleaned_data['postal_code'],
            city=form.cleaned_data['city'],
            state=form.cleaned_data['state'],
            country=form.cleaned_data['country'],
            address_book=book
        )

        # 3rd step - The member and user (when applied)
        member = Member.objects.create(
            name=form.cleaned_data['name'],
            surname=form.cleaned_data['surname'],
            member_no=form.cleaned_data['member_no'],
            date_of_birth=form.cleaned_data['date_of_birth'],
            email=form.cleaned_data['email'],
            telephone=form.cleaned_data['telephone'],
            status=form.cleaned_data['status'],
            picture=form.cleaned_data['picture'],
            nationality=form.cleaned_data['nationality'],
            has_user=form.cleaned_data['generate_user'],
            address_book=book
        )
        self.member = member

        if form.cleaned_data['generate_user']:
            user = User.objects.create_user(
                username=form.cleaned_data['member_no'],
                first_name=form.cleaned_data['name'],
                last_name=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                password="init1234"
            )

        return super().form_valid(form)


class MemberDetail(UpdateView, UserAuthMixin):
    """
    View for displaying a member
    """
    template_name = 'members/memberdetail.html'
    model = Member

    def get_context_data(self, **kwargs):
        """
        Returns the Member data based on member No.
        """
        context = super().get_context_data(**kwargs)
        member = Member.objects.get(member_no=self.kwargs['member_no'])
        context['member'] = member
        context['address_book'] = Address.objects.filter(address_book=member.address_book)
        return context
    
    def form_valid(self):
        """
        Updates member's details
        """
        super().form_valid(**kwargs)

    def get_success_url(self):
        """
        Returns to member's list
        """
        return reverse('member:list', context)


class MemberList(ListView, UserAuthMixin):
    """
    View to list all members
    """
    model = Member
    template_name = 'members/fullmemberlist.html'
