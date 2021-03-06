from random import  sample
import re

from django.conf import settings
from django.http import HttpResponse, HttpResponsePermanentRedirect, Http404
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import slugify

from boats.models import Boat
from boats.forms import ContactForm
import requests

def index(request):
    if request.method == 'POST':
        recaptcha_data = {
            'secret': settings.RECAPTCHA_SECRET,
            'response': request.POST[u'g-recaptcha-response']
        }

        try:
            recaptcha_api = requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=recaptcha_data
                ).json()
        except:
            recaptcha_api = {'success': False}

        if not recaptcha_api['success']:
            return HttpResponse("reCaptcha error. Please try again.")

        form = ContactForm(request.POST)

        if form.is_valid():
            subject = "[CBNJ] Contact Form Info - %s" % form.cleaned_data['email']
            lines = []
            lines.append("First Name: %s" % form.cleaned_data['first_name'])
            lines.append("Last Name: %s" % form.cleaned_data['last_name'])
            lines.append("E-mail: %s" % form.cleaned_data['email'])
            lines.append("Subject: %s" % form.cleaned_data['subject'])
            lines.append("\nMessage:\n%s" % form.cleaned_data['message'])

            body = "\n".join(lines)
            emails = ["foamranger@verizon.net", "ellieob@gmail.com", "tmh.2790@gmail.com"]

            try:
                send_mail(subject, body, "Boat Bot classicboatsnj@gmail.com", emails)
            except:
                return HttpResponse("Mail server error.<br />Please try again later.")
            return HttpResponse("OK")

        messages = []

        for field in form:
            for error in field.errors:
                messages.append(error)

        messages[-1] += "<br />"
        messages = "<br />\n".join(messages)

        return HttpResponse(messages)

    elif request.method == 'GET':
        form = ContactForm()
        context = {
            'boats': list(Boat.objects.order_by('order')),
            'form': form
        }

        return render(request, 'boats/index.html', context)


def boat_view(request, boat_url):
    attempt_redirect = False

    try:
        boat_instance = Boat.objects.get(url_name=boat_url)
    except ObjectDoesNotExist:
        attempt_redirect = True

    if attempt_redirect:
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', boat_url)
        s2 = re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1)
        clean_url = slugify(s2)
        try:
            Boat.objects.get(url_name=clean_url)
        except ObjectDoesNotExist:
            return Http404()
        return HttpResponsePermanentRedirect(reverse('boat', args=[clean_url]))

    next_url = boat_instance.get_next().url_name
    previous_url = boat_instance.get_previous().url_name
    other_boats = Boat.objects.exclude(url_name=boat_url)

    try:
        four_random_boats = sample(other_boats, 4)
    except:
        four_random_boats = []

    context = {
        'boat': boat_instance,
        'four_random_boats': four_random_boats,
        'previous_url': previous_url,
        'next_url': next_url,
    }

    return render(request, 'boats/boat.html', context)
