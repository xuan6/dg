import os
import gdata.media
import gdata.youtube.service
import pickle

from django.core.management import setup_environ
import dg.settings
setup_environ(dg.settings)

DEVELOPER_KEY = dg.settings.DEVELOPER_KEY
yt_service = gdata.youtube.service.YouTubeService()
yt_service.email = dg.settings.EMAIL
yt_service.password = dg.settings.PWD
yt_service.source = 'my-example-application'
yt_service.developer_key = DEVELOPER_KEY
yt_service.ProgrammaticLogin()
yt_service.ssl = True


def upload(file_name):
    my_media_group = gdata.media.Group(
            title=gdata.media.Title(text=str(file_name)),
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
    video_file_location = "".join([dg.settings.MEDIA_ROOT, 'videos/' + 'complete' + file_name])
    
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


def combine(file_name):
    print "in combine function"
    pickle_file_name = dg.settings.MEDIA_ROOT + 'videos/' + file_name + '_pickle.p'
    dict = pickle.load(open(pickle_file_name, "rb" ))
    print "after pickle file"
    total_chunks = dict['total_chunks']
    print dict
    print total_chunks
    #destination = open(dg.settings.MEDIA_ROOT + 'video/' + 'complete' + file_name, 'ab+')
    for i in range(1, int(total_chunks) + 1):
        print "1"
        print dg.settings.MEDIA_ROOT + 'videos/' + 'complete' + file_name
        destination = open(dg.settings.MEDIA_ROOT + 'videos/' + 'complete' + file_name, 'ab')
        source = open(dg.settings.MEDIA_ROOT + 'videos/' + str(i) + file_name, 'rb')
        destination.write(source.read())
        print "2"
        source.close()
        destination.close()
        os.remove(dg.settings.MEDIA_ROOT + 'videos/' + str(i) + file_name)
        print i
    return upload(file_name)



