from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from ban.models import Ban


USER_MODEL = get_user_model()


class ExtendedUserAdmin(UserAdmin):
    actions = ['ban_selected_users_permanently']

    def ban_selected_users_permanently(self, request, queryset):
        for user in queryset:
            Ban.objects.create(receiver=user, creator=request.user)
        self.message_user(request, "Successfully banned selected users permanently.")


class BanAdmin(admin.ModelAdmin):
    list_display = ('receiver', 'end_date', 'creator')


admin.site.unregister(USER_MODEL)
admin.site.register(USER_MODEL, ExtendedUserAdmin)

admin.site.register(Ban, BanAdmin)
