"""User App Models"""
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse

NAME_REGEX = RegexValidator(
    regex=r'^[a-zA-Z ]+$',
    message="Name should only consist of english alphabets")

PHONE_REGEX = RegexValidator(regex=r'^\d{10,10}$',
                             message="Phone number must be of 10 digits")

# Regular Expression Validators for name and phone number


class UserManager(BaseUserManager):
    """
    Custom User Manager.Inherits BaseUserManager.
    Used to add user's by the django admin
    """

    def _create_user(self, member_id, email, password, is_superuser, **extra_fields):

        if not email:
            raise ValueError('Email must be set')
        if not member_id:
            raise ValueError('Member ID must be set')

        email = email.lower()
        member_id = member_id.lower()

        user = self.model(email=email, member_id=member_id,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, member_id, email, password, **extra_fields):
        return self._create_user(member_id, email, password, False, **extra_fields)

    def create_superuser(self, member_id, email, password, **extra_fields):
        return self._create_user(member_id, email, password, True, **extra_fields)


class User(AbstractBaseUser):
    """
    Custom User Model.The login field will be college id and password.
    is_superuser - The user is a django admin(staff)
    is_faculty - The user is a faculty member
    """
    member_id = models.CharField(
        verbose_name='College ID',
        max_length=20,
        unique=True,
    )
    email = models.EmailField(max_length=255, unique=True)

    first_name = models.CharField(validators=[NAME_REGEX], max_length=30)
    last_name = models.CharField(validators=[NAME_REGEX], max_length=30)
    is_faculty = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = 'member_id'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'email',
        'is_faculty'
        ]

    def get_full_name(self):
        return u''.join(self.first_name)

    def get_short_name(self):
        return self.first_name

    def __unicode__(self):
        return self.email

    def has_perm(perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

    def get_absolute_url(self):
        return reverse('update_profile', kwargs={'pk': self.id})

