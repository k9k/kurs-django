from django.db import models
#from django.contrib.auth.models import User
from shelf.models import BookItem
from django.conf import settings

from django.utils.timezone import now

# Create your models here.

class Rental(models.Model):
    who = models.ForeignKey(settings.AUTH_USER_MODEL)   # 'django.contrib.auth.User'
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now())  #lub auto_now_add=True
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{who}, {what}, {when}".format(who=self.who, what=self.what, when=self.when)