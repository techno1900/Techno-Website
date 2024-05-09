from django.shortcuts import render,redirect
from .forms import ContactForm
# Create your views here.

def contact(req):
    form = ContactForm()
    if req.method == "POST":
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('service')
    context = {'form':form}
    return render(req, 'contact/contact.html', context)
