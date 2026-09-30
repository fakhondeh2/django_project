from django.contrib import admin

from tag.models import tag


# Register your models here.




class TagAdmin(admin.ModelAdmin):

    list_display = ['__str__','title','slug', 'active','time']
    class Meta:
        model = tag


admin.site.register(tag, TagAdmin)
