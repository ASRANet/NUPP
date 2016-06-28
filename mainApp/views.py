# -*- coding: UTF-8 -*-

from django.shortcuts import render
from mainApp.models import SiteSetting, Item


def index(request):
    story_list = Item.objects.filter(page__name="index").order_by('order')
    site_settings = SiteSetting.objects.all().first()

    return render(request, 'index.html', {"story_list": story_list, "title": "Home", "site_settings": site_settings,
                                          "page": "index"})


def venue(request):
    story_list = Item.objects.filter(page__name="venue").order_by('order')
    site_settings = SiteSetting.objects.all().first()
    return render(request, 'venue.html', {"story_list": story_list, "title": "Venue", "site_settings": site_settings})


def author_instructions(request):
    site_settings = SiteSetting.objects.all().first()

    story_list = [{"headline": "Speaker Information",
                  "id": "SpeakerInformation",
                   "table_class":
                       "<ul><li>Presentations should be in MS PowerPoint or PDF format. Please keep the use"
                       " of video and audio to a minimum as it could prove problematic.</li>"
                       "<br>"
                       "<li>All presentations should be emailed to us a week before the conference. If authors wish"
                       " to make any changes to their presentations please let us know as soon as possible and send"
                       "the relevant files to us at least 24 hours before you are due to speak.</li>"
                       "<br>"
                       "<li>The timeslots allocated to presenters are 20min: 15 minutes for your presentation and a"
                       " further 5 minutes for questions from the audience. The session chairs will remind you when"
                       " your time has finished. Please keep these times in mind.</li>"
                       "<br>"
                       "<li>All speakers should be in the relevant room, in which their presentation will take"
                       " place, at least 5 minutes before their session starts.</li>"
                       "<br>"
                       "<li>Please note that speakers are not exempt from registration fees.</li></ul>"},

                  {"headline": "Author Information",
                  "id": "AuthorInformation",
                   "table_class":
                       "<ul><li>Please submit all papers by 22 July 2016 by emailing them to us. If you are worried "
                       "about making the deadline then please contact us, so that an extension can be arranged.</li>"
                       "<br>"
                       "<li><a href='/static/paperFormat.doc'>Here is the official template</a> to use for all papers."
                       " This template can also be used for abstracts.</li>"
                       "<br>"
                       "<li>All papers should be submitted in PDF format and should not be numbered. There is no "
                       "specific page number requirement for papers, although most tend to be around the 8 "
                       "page mark.</li>"
                       "<br>"
                       "<li>In addition, you must also fill out and sign a Copyright Release form "
                       "<a href='/static/copyrightForm.doc'>(found here)</a> and email a scanned copy of that to us, "
                       "so that your paper can be included in the Official Conference Proceedings.</li>"
                       "<br>"
                       "<li>Please note that authors are not exempt from registration fees. Any additional co-authors "
                       "that wish to attend the conference are subject to a discounted rate.</li></ul>"},

                  {"headline": "Exhibitor Information",
                  "id": "ExhibitorInformation",
                   "table_class":
                       "<ul><li>All exhibitors should arrive at the conference venue at least half an hour before the "
                       "conference starts on Day 1.</li>"
                       "<br>"
                       "<li>All material that exhibitors wish to display should be supplied by the exhibitor and "
                       "relevant delivery and collection services to the venue arranged.</li>"
                       "<br>"
                       "<li>Please let us know when delivery is scheduled, so that we can make sure to make venue "
                       "staff aware.</li>"
                       "<br>"
                       "<li>Should you want to bring heavy/bulky exhibits please let us know beforehand as this "
                       "may not be possible in all cases.</li>"
                       "<br>"
                       "<li>All exhibition packages include a free registration, so you can take part in conference "
                       "sessions. All breaks will take place in the exhibition room(s).</li></ul>"},
                  ]

    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": story_list,
                                                               "site_settings": site_settings}, )


def accomodation(request):
    site_settings = SiteSetting.objects.all().first()
    return render(request, 'accomodation.html', {"site_settings": site_settings})


def contactus(request):
    site_settings = SiteSetting.objects.all().first()
    return render(request, 'contactUs.html', {"site_settings": site_settings})


def otherconferences(request):
    site_settings = SiteSetting.objects.all().first()
    return render(request, 'otherConferences.html', {"site_settings": site_settings})


def travel(request):
    story_list = Item.objects.filter(page__name="travel").order_by('order')
    site_settings = SiteSetting.objects.all().first()
    return render(request, 'baseTemplates/infoPageBase.html', {"story_list": story_list, "title": "Travel",
                                                               "site_settings": site_settings})


def cookies(request):
    site_settings = SiteSetting.objects.all().first()
    return render(request, 'cookies.html', {"site_settings": site_settings})


def robots(request):
    return render(request, 'robots.txt')
