import re

from django.db import models, OperationalError
from django.dispatch import receiver
from django.template.defaultfilters import slugify

def default_order():
    try:
        return Boat.objects.aggregate(models.Max('order')) + 1
    except OperationalError:
        return -1

class Boat(models.Model):
    order = models.IntegerField(default=0, editable=False)
    url_name = models.CharField(max_length=255)
    nice_name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    post_text = models.TextField()
    main_image = models.ImageField()

    def __unicode__(self):
        from django.utils.text import slugify
        print slugify("%s - %s" % (self.nice_name, self.subtitle))
        return "%s - %s" % (self.nice_name, self.subtitle)

    def get_subtitle_list(self):
        return self.subtitle.split('/')

    def get_next(self):
        next_boat = Boat.objects.filter(id__gt=self.id).order_by('id').first()
        if not next_boat:
            next_boat = Boat.objects.order_by('id').first()
        return next_boat

    def get_previous(self):
        previous_boat = Boat.objects.filter(id__lt=self.id).order_by('-id').last()
        if not previous_boat:
            previous_boat = Boat.objects.order_by('id').last()
        return previous_boat

    def _move_order(self, amount):
        assert amount != 0

        if amount > 0:
            aggregate_extreme = Boat.objects.aggregate(models.Max('order')).get('order__max')
        else:
            aggregate_extreme = Boat.objects.aggregate(models.Min('order')).get('order__min')

        if self.order == aggregate_extreme:
            return

        Boat.objects.filter(id=self.id).update(order=models.F('order')+amount)
        updated_boat = Boat.objects.get(id=self.id)
        Boat.objects.filter(order=updated_boat.order).exclude(id=self.id).update(order=models.F('order')-amount)

    def move_order_down(self):
        self._move_order(1)

    def move_order_up(self):
        self._move_order(-1)

@receiver(models.signals.pre_save, sender=Boat)
def boat_pre_save(instance, *args, **kwargs):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', instance.url_name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1)
    instance.url_name = slugify(s2)

class Image(models.Model):
    boat = models.ForeignKey('Boat')
    ordering = models.IntegerField(null=True)
    image_file = models.ImageField()
