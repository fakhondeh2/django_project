from django.contrib import admin

from tag.models import Tag


# Register your models here.




class TagAdmin(admin.ModelAdmin):

    list_display = ['__str__','id','title','slug', 'active','time']
    class Meta:
        model = Tag


admin.site.register(Tag, TagAdmin)
