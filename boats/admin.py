from django.contrib import admin

from .models import Boat, Image

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1
    ordering = ('ordering',)
    exclude = ('ordering',)


class BoatAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(Boat, BoatAdmin)
