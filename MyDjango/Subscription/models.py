from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class UserInfo(models.Model):
    userAccount = models.CharField(max_length=200, primary_key=True)
    userBirth = models.DateTimeField('Birthday')
    userSubDate = models.DateTimeField('Subscription date')

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.userAccount