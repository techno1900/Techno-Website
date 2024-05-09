from django.contrib import admin
from .models import AboutUs, OurService, Package, PackageContent

admin.site.register(AboutUs)
admin.site.register(OurService)
admin.site.register(Package)
admin.site.register(PackageContent)
# Register your models here.
