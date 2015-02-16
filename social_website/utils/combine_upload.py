import os
import gdata.media
import gdata.youtube.service

import dg.settings
from social_website.models import VideoChunk, VideoFile


def combine(file_identifier):
    video = VideoFile.objects.get(file_identifier=file_identifier)
    if video.total_chunks == VideoChunk.objects.filter(video_file=video).count():
        for i in range(1, video.total_chunks + 1):
            destination = open(dg.settings.MEDIA_ROOT + '/videos/' + video.file_name, 'ab')
            source = open(dg.settings.MEDIA_ROOT + '/videos/' + str(i) + video.file_name, 'rb')
            destination.write(source.read())
            source.close()
            destination.close()
            os.remove(dg.settings.MEDIA_ROOT + '/videos/' + str(i) + video.file_name)
            #return upload(file_name)
        video.combine = True
        video.save()
        #return upload(file_identifier)
        return "File Combined"
    else:
        return "Error in Combining File"



