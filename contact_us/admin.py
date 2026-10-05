from django.contrib import admin

from contact_us.models import ContactUs


# Register your models here.

class ContactusAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','fullName','time', 'read']
    class Meta:
        model = ContactUs


admin.site.register(ContactUs, ContactusAdmin)