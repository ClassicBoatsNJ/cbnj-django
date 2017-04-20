from django.conf.urls import url
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.html import format_html

from boats.models import Boat, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1
    ordering = ('ordering',)
    exclude = ('ordering',)


class BoatAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    ordering = ('order',)
    list_display = ('id', '__unicode__', 'boat_actions')
    list_display_links = ('__unicode__',)
    readonly_fields = ('boat_actions',)

    def get_urls(self):
        urls = super(BoatAdmin, self).get_urls()
        custom_urls = [
            url(r'^(?P<boat_id>.+)/move-up/$', self.admin_site.admin_view(self.move_up), name='boat-move-up'),
            url(r'^(?P<boat_id>.+)/move-down/$', self.admin_site.admin_view(self.move_down), name='boat-move-down'),
        ]
        return custom_urls + urls

    def boat_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Move Up</a>&nbsp;'
            '<a class="button" href="{}">Move Down</a>',
            reverse('admin:boat-move-up', args=[obj.pk]),
            reverse('admin:boat-move-down', args=[obj.pk]),
        )
    boat_actions.short_description = 'Actions'
    boat_actions.allow_tags = True

    def move_up(self, request, boat_id):
        boat = Boat.objects.get(id=boat_id)
        boat.move_order_up()
        return HttpResponseRedirect(reverse('admin:boats_boat_changelist'))

    def move_down(self, request, boat_id):
        boat = Boat.objects.get(id=boat_id)
        boat.move_order_down()
        return HttpResponseRedirect(reverse('admin:boats_boat_changelist'))


admin.site.register(Boat, BoatAdmin)
