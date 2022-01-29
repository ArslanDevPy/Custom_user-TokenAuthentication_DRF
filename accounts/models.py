from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(_('username'), max_length=150, unique=True, null=True, blank=True,
                                validators=[username_validator],
                                help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                                error_messages={'unique': _("A user with that username already exists."), }, )
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'users'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """ Sends an email to this User. """
        send_mail(subject, message, from_email, [self.email], **kwargs)
