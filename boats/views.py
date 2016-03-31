from random import shuffle, sample

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail

from .models import Boat
from .forms import ContactForm
import requests as outbound_requests

ALL_BOATS = [boat for boat in Boat.objects.all().order_by("-id")]
def index(request):
    if request.method == 'POST':
        request.POST
        recaptcha_data = {
            'secret': settings.RECAPTCHA_SECRET,
            'response': request.POST[u'g-recaptcha-response']
            }
        try:
            recaptcha_api = outbound_requests.post(
                "https://www.google.com/recaptcha/api/siteverify",
                data=recaptcha_data
                ).json()
        except:
            recaptcha_api = {'success': False}
        if recaptcha_api['success']  != True:
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
            'boats': ALL_BOATS,
            'form': form
        }
        return render(request, 'boats/index.html', context)


def boat(request, boat_url):
    boat_instance = get_object_or_404(Boat, url_name=boat_url)
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
