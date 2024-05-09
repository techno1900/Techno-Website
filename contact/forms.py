from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name','email','description']

    def __init__(self, *args, **kwrgs):
        super(ContactForm, self).__init__(*args, **kwrgs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control border-0 bg-light px-4', 'placeholder':'First Name', 'style':'height: 55px'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control border-0 bg-light px-4', 'placeholder':'Last Name', 'style':'height: 55px'})
        self.fields['email'].widget.attrs.update({'class':'form-control border-0 bg-light px-4', 'placeholder':'Email', 'style':'height: 55px'})
        self.fields['description'].widget.attrs.update({'class':'form-control border-0 bg-light px-4 py-3', 'placeholder':'Description', 'style':'height: 55px'})