from django.contrib import admin

from slsiders.models import Slsider


# Register your models here.



class SlsiderAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','title', 'active','time']
    class Meta:
        model = Slsider


admin.site.register(Slsider, SlsiderAdmin)