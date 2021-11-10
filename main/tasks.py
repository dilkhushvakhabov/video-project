import ffmpeg
from celery import shared_task
from .models import Video, VideoQuality


RESOLUTIONS = [
    (240, 426),
    (360, 480),
    (720, 1280),
    (1080, 1920),
]

"""
2160p=3840x2160
1440p=2560×1440
1080p=1920×1080 
720p=1280×720   
480p=640×480    
360p=480×360    
240p=426×240    
144p=256×144  
"""
@shared_task
def add(x, y):
    return x + y


@shared_task
def convert_file(file_path, instance_id):
    for resolution in RESOLUTIONS:
        height, width = resolution
        new_filename = file_path.split('.')[0].split('/')[-1]
        full_path_with_name = f"media/video/{new_filename}_{height}p.mp4"
        stream = ffmpeg.input(file_path)
        stream = ffmpeg.filter(stream, 'scale', height=f"{height}", width=f"{width}")
        stream = ffmpeg.output(stream, full_path_with_name)
        ffmpeg.run(stream)
        video_instance = Video.objects.get(id=instance_id)
        full_path_with_name = full_path_with_name.replace('media/', '')
        VideoQuality.objects.create(video=video_instance, file=full_path_with_name, resolution=f'{height}p')

