import os
import gdata.media
import gdata.youtube.service

import dg.settings
from social_website.models import VideoChunk, VideoFile


def upload(file_identifier):
    DEVELOPER_KEY = dg.settings.DEVELOPER_KEY
    yt_service = gdata.youtube.service.YouTubeService()
    yt_service.email = dg.settings.EMAIL
    yt_service.password = dg.settings.PWD
    yt_service.source = 'my-example-application'
    yt_service.developer_key = DEVELOPER_KEY
    yt_service.ProgrammaticLogin()
    yt_service.ssl = True
    my_media_group = gdata.media.Group(
            title=gdata.media.Title(text=str(file_identifier)),
            description=gdata.media.Description(description_type='plain', text='We shall provide it'),
            keywords=gdata.media.Keywords(text='subject, topic'),
            category=[gdata.media.Category(
                                           text='Autos',
                                           scheme='http://gdata.youtube.com/schemas/2007/categories.cat',
                                           label='Autos')],
            player=None
            )
    # create the gdata.youtube.YouTubeVideoEntry to be uploaded
    video_entry = gdata.youtube.YouTubeVideoEntry(media=my_media_group)
    # set the path for the video file binary
    video_file_location = "".join([dg.settings.MEDIA_ROOT, '/videos/' + 'complete' + file_identifier])
    print "uploading videos"
    new_entry = yt_service.InsertVideoEntry(video_entry, video_file_location)
    link = new_entry.media.player.url
    print link
    import urlparse
    parsed = urlparse.urlparse(link)
    youtube_id = urlparse.parse_qs(parsed.query)['v'][0]
    youtube_link = link
    print youtube_id
    return youtube_link


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
        video.upload = True
        video.save()
        #return upload(file_identifier)
        return('abcd')
    else:
        return "error in uploading file"



