"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from mainApp import views as main_views


class HomeSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class PrioritySitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['contactus', 'register', 'uploadAbstract']

    def location(self, item):
        return reverse(item)


class Sitemaps(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['venue', 'accomodation', 'travel', 'cookies']

    def location(self, item):
        return reverse(item)


sitemaps = {
    'homepage': HomeSitemap,
    'priority': PrioritySitemap,
    'static': Sitemaps,
}

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^venue/', main_views.venue, name='venue'),
    url(r'^accomodation/', main_views.accomodation, name='accomodation'),
    url(r'^contactus/', main_views.contactus, name='contactus'),
    url(r'^travel/', main_views.travel, name='travel'),
    url(r'^register/', include('register.urls')),
    url(r'^uploadAbstract/', include('uploadAbstract.urls')),
    url(r'^authorinstructions/', main_views.author_instructions, name='authorInstructions'),
    url(r'^cookies/', main_views.cookies, name='cookies'),
    url(r'^$', main_views.index, name='index'),
    url(r'^index', main_views.index, name='index'),
    url(r'^robots\.txt$', main_views.robots, name='robots'),
    url(r'^otherconferences/', main_views.otherconferences, name='otherconferences'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]

