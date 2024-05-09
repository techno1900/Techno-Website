from django.shortcuts import render
from. models import AboutUs,OurService, Package, PackageContent

# Create your views here.
def service(req):
    about = AboutUs.objects.all()
    service = OurService.objects.all()
    package = Package.objects.all()
   
    
    context = {'about':about, 'service':service, 'package':package}
    return render(req, 'services/services.html', context)

