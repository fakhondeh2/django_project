from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs


def contact_us_view(request):
    context = {
        "contact_form": ContactForm()
    }
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            fullname = contact_form.cleaned_data.get('fullname')
            email = contact_form.cleaned_data.get('email')
            message = contact_form.cleaned_data.get('message')

            new_contact = ContactUs.objects.create(fullName=fullname, email=email, message=message)

            if new_contact:
                context = {
                    "contact_form": ContactForm(),
                    "success_message": "پیام شما با موفقیت ثبت شد."
                }

    return render(request, "contact_us_page.html", context)