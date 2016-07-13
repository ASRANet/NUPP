from __future__ import unicode_literals
from django.db import models
from NUPP.email_functionality import email_admin, email_client
from mainApp.models import SiteSetting

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO


class User(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    organisation = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=60)
    telephone = models.CharField(max_length=15)
    email = models.EmailField(max_length=60, unique=True)
    registration_fee = models.CharField(max_length=30)
    discount_code_if_applicable = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        sorted_self = [["Salutation", self.salutation], ["First name", self.first_name], ["Last Name", self.last_name],
                       ["Email", self.email], ["Telephone", self.telephone], ["Address", self.address],
                       ["City", self.city], ["Country", self.country], ["Postcode", self.postcode],
                       ["Organisation", self.organisation], ["Registration Fee", self.registration_fee],
                       ["Discount Code", self.discount_code_if_applicable]]

        site_settings = SiteSetting.objects.all().first()

        email_client(self, site_settings.site_name + "Conference Registration", "You are officially registered for NUPP 2017")
        email_admin(self, "New " + site_settings.site_name + " Registrant",
                    "Please find enclosed the details for the new NUPP 2017registrant.",
                    sorted_self)

        super(User, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email
