from django.db import models


class Boat(models.Model):
    url_name = models.CharField(max_length=255)
    nice_name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    post_text = models.TextField()
    main_image = models.ImageField()

    def __unicode__(self):
        return "%s - %s" % (self.nice_name, self.subtitle)

    def get_subtitle_list(self):
        return self.subtitle.split('/')

    def get_next(self):
        try:
            next_object = Boat.objects.filter(id__gt=self.id).order_by('id')[0]
        except:
            next_object = Boat.objects.order_by('id').first()
        return next_object

    def get_previous(self):
        try:
            previous_object = Boat.objects.order_by('-id').filter(id__lt=self.id)[0]
        except:
            previous_object = Boat.objects.order_by('id').last()
        return previous_object


class Image(models.Model):
    boat = models.ForeignKey('Boat')
    ordering = models.IntegerField(null=True)
    image_file = models.ImageField()
