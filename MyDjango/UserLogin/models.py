from django.db import models
from registration.models import UserInfo
# Create your models here.

class MyBackend(object):

    def authenticate(self, username=None, password=None) :
        return 0