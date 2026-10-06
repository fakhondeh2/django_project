from django.shortcuts import render

from .forms import ContactForm
from .models import ContactUs

# Create your views here.


def contact_us_view(request):
    conact_form = ContactForm(request.POST or None)
    if conact_form.is_valid():
        fullname = conact_form.cleaned_data.get('fullname')
        email = conact_form.cleaned_data.get('email')
        message = conact_form.cleaned_data.get('message')
        new_contact = ContactUs.objects.create(fullName=fullname, email=email, message=message)
        if new_c

        print(new_contact)
    context={
        "contact_form":conact_form,
    }
    return render(request , "contact_us_page.html",context)