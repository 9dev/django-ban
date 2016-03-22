from django.conf import settings
from django.db import models


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Ban(models.Model):
    receiver = models.ForeignKey(USER_MODEL, unique=True)
    creator = models.ForeignKey(USER_MODEL, related_name='creator')
    end_date = models.DateTimeField(null=True, blank=True, default=None)
