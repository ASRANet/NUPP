from __future__ import unicode_literals
from NUPP.email_functionality import email_admin, email_client
from django.db import models


class SubmittedAbstract(models.Model):
    salutation = models.CharField(max_length=6)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    co_authors_names = models.CharField(max_length=770)
    email = models.EmailField(max_length=60, unique=True)
    paper_title = models.CharField(max_length=60)
    abstract = models.CharField(max_length=2000)

    def save(self, *args, **kwargs):

        sorted_self = [["Salutation", self.salutation], ["Primary Author First Name", self.first_name],
                       ["Primary Author Surname", self.last_name],
                       ["Co Authors Names", self.co_authors_names], ["Email", self.email],
                       ["Paper Title", self.paper_title], ["Abstract", self.abstract],
                       ]

        email_client(self, "AdWind 2017 Abstract Upload", "Thank you for uploading your abstract to AdWind 2017")
        email_admin(self, "New AdWind 2017 Abstract", "Please find enclosed the details for the new AdWind "
                                                      "2017 abstract upload.", sorted_self)

        super(SubmittedAbstract, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email
