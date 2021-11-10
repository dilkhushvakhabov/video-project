from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='video/')

    def __str__(self):
        return self.title


class VideoQuality(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='resolutions')
    file = models.FileField(upload_to='video/')
    resolution = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id} - {self.resolution}'
