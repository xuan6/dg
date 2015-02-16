from django.core.management.base import BaseCommand, CommandError

from libs.youtube_utils import upload
from social_website.models import VideoFile


class Command(BaseCommand):
    help = '''Run this command when some video from dashboard is not in website tables'''

    def handle(self, *args, **options):
        vids_not_uploaded = VideoFile.objects.filter(combine=1, upload=0)
        for vid in vids_not_uploaded:
            upload(vid)
