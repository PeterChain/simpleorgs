from django.contrib import admin

from .models import Member, MemberStatus

admin.site.register(MemberStatus)
admin.site.register(Member)