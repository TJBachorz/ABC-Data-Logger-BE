from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, Case, CaseLink


class AccountAdmin(UserAdmin):
    list_display = ('id', 'email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.

admin.site.register(Account, AccountAdmin)
admin.site.register(Case)
admin.site.register(CaseLink)