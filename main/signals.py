from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .tasks import convert_file
from .models import Video


@receiver(post_save, sender=Video)
def save_video(sender, instance, created, **kwargs):
    if created:
        path = f"{settings.MEDIA_ROOT}/{instance.file.name}"
        convert_file.delay(path, instance.id)
