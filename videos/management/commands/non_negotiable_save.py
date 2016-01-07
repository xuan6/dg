import os
from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model

from dg.settings import MEDIA_ROOT

from videos.scripts.convert_to_docx import save_as_document

class Command(BaseCommand):

	def handle(self, *args, **options):
		#For all video in with non-negotiables page create files
		video_list = []
		NonNegotiable = get_model('videos', 'NonNegotiable')
		nonnegotiable_objects = NonNegotiable.objects.all()
		for obj in nonnegotiable_objects:
			video_id = obj.video.id
			if video_id not in video_list:
				video_list.append(video_id)
		save_as_document(video_list[1])
		#for vid in video_list:
			#save_as_document(vid)
