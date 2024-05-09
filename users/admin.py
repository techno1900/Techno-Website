from django.contrib import admin
from .models import UserAccount
from django.contrib.auth.admin import UserAdmin

class UserAccountAdmin(UserAdmin):
    list_filter = ()
    filter_horizontal = ()
    fieldsets = ()
admin.site.register(UserAccount, UserAccountAdmin)
# Register your models here.
