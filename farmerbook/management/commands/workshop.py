from django.core.management.base import BaseCommand

from activities.models import *
from people.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        videos = [2969, 3022]
        person_comment_one = {
        98333: "what is the cost involved ?",
        75619: 'Is it too costly ?',
        67200: "Can we afford it ?",
        86698: 'Benefits of hand washing is not clear ?',
        86707: 'Is special soap needed?',
        72545: 'Cost seems to be high',
        86662: 'Too expensive ?',
        72456: 'Type of soap to be used?',
        116065: 'Benefits is unclear',
        72023: 'Required type of soap?',
        70320: "how expensive a soap is ?",
        71977: "At what price can we buy a hand washing soap ?",
        86648: 'Too expensive',
        68261: 'Is special soap needed?',
        86673: 'Cost is too high',
        72053: "Couldn't understand the benefits",
        65424: 'Expensive ?'
        }
        person_comment_two = {
        95437: "No info about tablets being free of cost under govt scheme",
        95455: "Don't know about tablets",
        65530: "Family members won't allow",
        98333: "Unaware about tablets availability from govt",
        72567: "Anganwadi is too far",
        72488: "Family members stops me",
        72512: "How can we get these tablets ?",
        72517: "Does govt. provide these tablet or we need to buy ?",
        72648: "Family members dont allow to take them",
        72642: "Don't know much about tablets",
        75422: "Does govt provide these tablets ?",
        65604: "Anganwadi is too far",
        86606: "Family issues"
        }

        person_phone = {
        98333: "9582920239",
        75619: "9013623264",
        67200: "9810253264",
        86698: "9871245783",
        86662: "9910338592",
        65530: "8826280343",
        72560: "7838372235",
        72495: "8826653998",
        72488: "9711692618"
        }

        print "*******************video 1***************************"
        for key, value in person_comment_one.iteritems():
            try:
                PersonMeetingAttendance.objects.filter(person_id=key).filter(
                    screening__videoes_screened__id=videos[0]).update(expressed_question=str(value))
                print key, "saved"
            except Exception as e:
                print key,  e

        print "*******************video 2***************************"
        for key, value in person_comment_two.iteritems():
            try:
                PersonMeetingAttendance.objects.filter(person_id=key).filter(
                    screening__videoes_screened__id=videos[1]).update(expressed_question=str(value))
                print key, "saved"
            except Exception as e:
                print key, e


        print "*******************phone***************************"
        for key, value in person_phone.iteritems():
            try:
                Person.objects.filter(id=key).update(phone_no=str(value))
                print key, "saved"
            except Exception as e:
                print key, e