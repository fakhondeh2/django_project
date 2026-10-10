from django.contrib import admin
from settings.models import Settings
# Register your models here.


class SettingsAdmin(admin.ModelAdmin):

    list_display = ['__str__','phone', 'address'
                    ]
    class Meta:
        model = Settings

admin.site.register(Settings, SettingsAdmin)