# -*- coding: utf-8 -*-

from django.contrib import admin

from show.models import User, Record
from django.utils import timezone
import datetime


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'password', 'log')  # list

    list_per_page = 50

    ordering = ('id',)

    readonly_fields = ('code', 'password', 'status', 'name_pinyin')

    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(status=1)
        else:
            return qs.filter(name_pinyin=request.user)


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('add_date', 'reporter', 'status')  # list

    list_per_page = 18

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_queryset(self, request):
        qs = super(RecordAdmin, self).get_queryset(request)

        return qs.filter(add_date__gt=(timezone.now() - datetime.timedelta(days=1)))
