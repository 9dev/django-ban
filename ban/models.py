from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Ban(models.Model):
    receiver = models.ForeignKey(USER_MODEL, unique=True)
    creator = models.ForeignKey(USER_MODEL, related_name='creator')
    end_date = models.DateTimeField(null=True, blank=True, default=None)


@receiver(pre_save, sender=Ban)
def on_save_approve(sender, instance, **kwargs):
    try:
        ban = Ban.objects.get(receiver=instance.receiver)
        if instance.end_date is None or instance.end_date > ban.end_date:
            ban.delete()
        else:
            instance.delete()
    except Ban.DoesNotExist:
        pass
