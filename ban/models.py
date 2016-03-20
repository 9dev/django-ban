from django.db import models


class Ban(models.Model):
    receiver = models.ForeignKey('auth.User', unique=True)
    creator = models.ForeignKey('auth.User', related_name='creator')
    end_date = models.DateTimeField(null=True, default=None)
