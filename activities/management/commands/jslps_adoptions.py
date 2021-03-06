import urllib2
import unicodecsv as csv
from datetime import datetime 
import xml.etree.ElementTree as ET
from django.core.management.base import BaseCommand
from people.models import *
from programs.models import *
from videos.models import *
from activities.models import *

class Command(BaseCommand):
	def handle(self, *args, **options):
		
		partner = Partner.objects.get(id = 24)
		url = urllib2.urlopen('http://webservicesri.swalekha.in/Service.asmx/GetExportAdoptionData?pUsername=admin&pPassword=JSLPSSRI')
		contents = url.read()
		xml_file = open("/home/ubuntu/code/dg_git/activities/management/adoption.xml", 'w')
		xml_file.write(contents)
		xml_file.close()

		csv_file = open('/home/ubuntu/code/dg_git/activities/management/adoption_error.csv', 'wb')
		wtr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
		tree = ET.parse('/home/ubuntu/code/dg_git/activities/management/adoption.xml')
		root = tree.getroot()
		for c in root.findall('AdoptionData'):
			pc = c.find('MemberCode').text
			vc = c.find('Video').text
			da = datetime.datetime.strptime(c.find('DOA').text, '%d/%m/%Y')
			de = datetime.datetime.strptime(c.find('DOE').text, '%d/%m/%Y')

			error = 0
			try:
				video = JSLPS_Video.objects.get(vc = vc)
			except JSLPS_Video.DoesNotExist as e:
				wtr.writerow(['video', vc, e])
				error = 1
			try:
				person = JSLPS_Person.objects.get(person_code = pc)
			except (JSLPS_Video.DoesNotExist, JSLPS_Person.DoesNotExist) as e:
				wtr.writerow(['person', pc, e])
				error = 1

			if(error==0):
				try:
					pap = PersonAdoptPractice(person = person.person,
											video = video.video,
											date_of_adoption = da,
											time_created = de,
											partner = partner)
					pap.save()
					print "pap saved"
				except Exception as e:
					print vc, pc, e
					wtr.writerow(['Adoption', 'Person', pc, 'Video', vc, e])
