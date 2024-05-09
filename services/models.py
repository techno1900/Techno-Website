from django.db import models
import uuid
# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    contact_number = models.CharField(max_length=20)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'aboutus'



class OurService(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="services/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.title


class Package(models.Model):
    plane = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    package_title = models.ManyToManyField("PackageContent", blank=True)
    def __str__(self):
        return self.plane


class PackageContent(models.Model):
    # package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
