import os

from docx import Document
from docx.shared import Inches

from dg.settings import MEDIA_ROOT

def save_as_document(video_id):
	document = Document()

	document.add_heading('Document Title', 0)
	p = document.add_paragraph('A plain paragraph having some ')
	p.add_run('bold').bold = True
	p.add_run(' and some ')
	p.add_run('italic.').italic = True

	document.add_heading('Heading, level 1', level=1)
	document.add_paragraph('Intense quote', style='IntenseQuote')

	document.add_paragraph(
		'first item in unordered list', style='ListBullet'
	)
	document.add_paragraph(
		'first item in ordered list', style='ListNumber'
	)

	document.add_page_break()

	filename = os.path.join(MEDIA_ROOT, "non_negotiables", "%s.docx" % (video_id))
	document.save(filename)
