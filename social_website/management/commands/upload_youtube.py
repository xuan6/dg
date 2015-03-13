from django.core.management.base import BaseCommand, CommandError

from boto.s3.connection import S3Connection

from dg.settings import ACCESS_KEY, SECRET_KEY, MEDIA_ROOT
from libs.youtube_utils import upload
from libs.s3_utils import add_to_s3
from social_website.models import VideoFile


class Command(BaseCommand):
    help = '''Run this command when some video from dashboard is not in website tables'''

    def handle(self, *args, **options):
        bucket_name = 'digitalgreenvideos'
        bucket = S3Connection(ACCESS_KEY, SECRET_KEY).create_bucket(bucket_name)
        bucket.set_acl('public-read')
        vids_not_uploaded = VideoFile.objects.exclude(coco_video__isnull=True).filter(combine=1, upload=0)
        for vid in vids_not_uploaded:
            upload(vid)
            key = "".join([str(vid.coco_video.id), '_', vid.coco_video.youtubeid])
            filepath = "".join([MEDIA_ROOT, '/videos/', str(vid.file_name)])
            add_to_s3(bucket, key, filepath)
