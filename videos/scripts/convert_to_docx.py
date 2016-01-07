import os

from docx import Document
from docx.shared import Inches

from django.db.models import get_model
from dg.settings import MEDIA_ROOT

from videos.scripts.exception_email import sendmail

def save_as_document(video_id):
	try:
		NonNegotiable = get_model('videos', 'NonNegotiable')
		nonnegotiables_list = NonNegotiable.objects.filter(video__id=video_id)
		Video = get_model('videos', 'Video')
		video_obj = Video.objects.get(id=video_id)

		document = Document()
		document.add_heading(video_obj.title, 0)
		for obj in nonnegotiables_list:
			text = obj.non_negotiable
			document.add_paragraph(text)
		
		#===================================================================
		# Formatting options:
		#
		# document.add_heading('Document Title', 0)
		# p = document.add_paragraph('A plain paragraph having some ')
		# p.add_run('bold').bold = True
		# p.add_run(' and some ')
		# p.add_run('italic.').italic = True
		# document.add_heading('Heading, level 1', level=1)
		# document.add_paragraph('Intense quote', style='IntenseQuote')
		# document.add_paragraph(
		# 	'first item in unordered list', style='ListBullet'
		# )
		# document.add_paragraph(
		# 	'first item in ordered list', style='ListNumber'
		# )
		# document.add_page_break()
		#===================================================================
		
		#saving file
		filename = os.path.join(MEDIA_ROOT, "non_negotiables", "%s.docx" % (video_id))
		document.save(filename)

	except Exception as e:
		error = "Video ID: "+str(video_id)+" Error: "+str(e)
		sendmail("Exception in creating document for Non Negotiables", error)
