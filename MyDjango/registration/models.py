from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    )
import datetime
from django.utils import timezone


class MyUserManager(BaseUserManager):
    def create_user(self, userAccount, userName, password=None):

        if not userAccount:
            raise ValueError('Users must have a account')
        user = self.model(
            userAccount=self.normalize_email(userAccount),
            userName=userName,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, userAccount, userName, password):
        user = self.create_user(
            userAccount=userAccount,
            userName=userName,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class UserInfo(AbstractBaseUser):

    sex_choice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    userAccount = models.EmailField(max_length=40, unique=True)
    userName = models.CharField(max_length=40)
    userSex = models.CharField(max_length=1, choices=sex_choice, null=True)
    userBirth = models.DateTimeField('Birthday', null=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'userAccount'
    REQUIRED_FIELDS = ['userName']

    objects = MyUserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.userAccount

    def get_short_name(self):
        # The user is identified by their email address
        return self.userAccount

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.userAccount

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin