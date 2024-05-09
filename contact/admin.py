from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display =['first_name', 'email', 'description', 'is_replyed']
    list_filter = ()
    list_editable = ['is_replyed']
admin.site.register(Contact, ContactAdmin)


# Register your models here.
