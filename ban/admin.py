from datetime import datetime, timedelta, timezone

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from ban.models import Ban, Warn


USER_MODEL = get_user_model()


class ExtendedUserAdmin(UserAdmin):
    actions = [
        'ban_selected_users_permanently',
        'ban_selected_users_for_month',
        'ban_selected_users_for_week',
        'ban_selected_users_for_day',
        'warn_selected_users',
    ]

    def warn_selected_users(self, request, queryset):
        for user in queryset:
            Warn.objects.create(receiver=user, creator=request.user)
        self.message_user(request, "Successfully warned selected users.")

    def ban_selected_users_permanently(self, request, queryset):
        for user in queryset:
            Ban.objects.create(receiver=user, creator=request.user)
        self.message_user(request, "Successfully banned selected users permanently.")

    def ban_selected_users_for_month(self, request, queryset):
        self._ban(request, queryset, 30)
        self.message_user(request, "Successfully banned selected users for a month.")

    def ban_selected_users_for_week(self, request, queryset):
        self._ban(request, queryset, 7)
        self.message_user(request, "Successfully banned selected users for a week.")

    def ban_selected_users_for_day(self, request, queryset):
        self._ban(request, queryset, 1)
        self.message_user(request, "Successfully banned selected users for a day.")

    def _ban(self, request, queryset, days):
        end_date = datetime.now(timezone.utc) + timedelta(days=days)
        for user in queryset:
            Ban.objects.create(receiver=user, creator=request.user, end_date=end_date)


class BanAdmin(admin.ModelAdmin):
    list_display = ('receiver', 'end_date', 'creator')


class WarnAdmin(admin.ModelAdmin):
    list_display = ('receiver', 'creator')


admin.site.unregister(USER_MODEL)
admin.site.register(USER_MODEL, ExtendedUserAdmin)

admin.site.register(Ban, BanAdmin)
admin.site.register(Warn, WarnAdmin)
