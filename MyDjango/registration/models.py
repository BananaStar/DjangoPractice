from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class UserInfo(models.Model):
    sex_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    dicUserInfo = {
        'userAccount': ('PK', 'email', 200),
        'userPassword': ('password', 20),
        'userName': ('text', 40),
        'userSex': ('radio', ('M', 'F'), 1),
        'userBirth': ('date'),
    }

    userAccount = models.CharField(max_length=200, primary_key=True)
    userPassword = models.CharField(max_length=20)
    userName = models.CharField(max_length=40)
    userSex = models.CharField(max_length=1, choices=sex_choice)
    userBirth = models.DateTimeField('Birthday')
    userRegDate = models.DateTimeField('Registration date')

    def FillInRegDate(self):
        self.userRegDate = timezone.now()

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.userAccount