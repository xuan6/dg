# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        Sector = orm['videos.PracticeSector']
        SubSector = orm['videos.PracticeSubSector']
        Topic = orm['videos.PracticeTopic']
        SubTopic = orm['videos.PracticeSubTopic']
        Subject = orm['videos.PracticeSubject']
        Practice = orm['videos.Practice']

        Sector.objects.bulk_create([Sector(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                           old_coco_id=x.id, name=x.name)for x in orm['dashboard.PracticeSector'].objects.all()])
        print "Sector Added"
        SubSector.objects.bulk_create([SubSector(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                                 old_coco_id=x.id, name=x.name)for x in orm['dashboard.PracticeSubSector'].objects.all()])
        print "SubSector Added"
        Topic.objects.bulk_create([Topic(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                         old_coco_id=x.id, name=x.name)for x in orm['dashboard.PracticeTopic'].objects.all()])
        print "Topic Added"
        SubTopic.objects.bulk_create([SubTopic(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                               old_coco_id=x.id, name=x.name)for x in orm['dashboard.PracticeSubTopic'].objects.all()])
        print "SubTopic Added"
        Subject.objects.bulk_create([Subject(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                             old_coco_id=x.id, name=x.name)for x in orm['dashboard.PracticeSubject'].objects.all()])
        print "Subject Added"

        Practice.objects.bulk_create([Practice(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                               old_coco_id=x.id, practice_name=x.practice_name, 
                                               practice_sector=None if x.practice_sector is None else Sector.objects.get(old_coco_id=x.practice_sector_id),
                                               practice_subsector=None if x.practice_subsector is None else SubSector.objects.get(old_coco_id=x.practice_subsector_id),
                                               practice_topic=None if x.practice_topic is None else Topic.objects.get(old_coco_id=x.practice_topic_id),
                                               practice_subtopic=None if x.practice_subtopic is None else SubTopic.objects.get(old_coco_id=x.practice_subtopic_id),
                                               practice_subject=None if x.practice_subject is None else Subject.objects.get(old_coco_id=x.practice_subject_id))
                                      for x in orm['dashboard.Practices'].objects.all()])
        print "Practices Added"

        db.create_index('videos_practice', ['old_coco_id'])

        print "index created for practices"

        Animator = orm['people.Animator']
        Language = orm['videos.Language']
        Village = orm['geographies.Village']
        Video = orm['videos.Video']

        Language.objects.bulk_create([Language(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                               old_coco_id=x.id, name=x.language_name) for x in orm['dashboard.Language'].objects.all()])

        print "Language Added"

        db.create_index('videos_language', ['old_coco_id'])
        print "index created for language"

        chunk = 1000
        dashboard_video = orm['dashboard.Video'].objects.all()
        for i in range(0, dashboard_video.count()/chunk + 1):
            dashboard_video_slice = dashboard_video[i*chunk:(i+1)*chunk]
            print "Video Added %d" % (i*chunk)
            Video.objects.bulk_create([Video(user_created_id=x.user_created_id, time_created=x.time_created, user_modified_id=x.user_modified_id, time_modified=x.time_modified,
                                             old_coco_id=x.id, title=x.title, video_type=x.video_type, duration=x.duration,
                                             language_id=Language.objects.get(old_coco_id=x.language_id).id,
                                             summary=x.summary, picture_quality=x.picture_quality, audio_quality=x.audio_quality,
                                             editing_quality=x.editing_quality, edit_start_date=x.edit_start_date, edit_finish_date=x.edit_finish_date,
                                             thematic_quality=x.thematic_quality, video_production_start_date=x.video_production_start_date,
                                             video_production_end_date=x.video_production_end_date, storybase=x.storybase,
                                             storyboard_filename=x.storyboard_filename, raw_filename=x.raw_filename, movie_maker_project_filename=x.movie_maker_project_filename,
                                             final_edited_filename=x.final_edited_filename,
                                             village_id=Village.objects.get(old_coco_id=x.village_id).id,
                                             facilitator_id=Animator.objects.get(old_coco_id=x.facilitator_id).id,
                                             cameraoperator_id=Animator.objects.get(old_coco_id=x.cameraoperator_id).id,
                                             approval_date=x.approval_date,
                                             #supplementary_video_produced_id = None if x.supplementary_video_produced_id is None else Video.objects.get(old_coco_id=x.supplementary_video_produced_id),
                                             video_suitable_for=x.video_suitable_for, remarks=x.remarks,
                                             related_practice_id = None if x.related_practice_id is None else Practice.objects.get(old_coco_id=x.related_practice_id).id,
                                             actors=x.actors, last_modified=x.last_modified, youtubeid=x.youtubeid, viewers=x.viewers,
                                             partner=orm['programs.Partner'].objects.get(old_coco_id=x.partner_id))
                                       for x in dashboard_video_slice])
        print "Videos Added"
        db.create_index('videos_video', ['old_coco_id'])
        print "index created for video"

        Farmer_Shown = Video.farmers_shown.through
        
        dashboard_farmer_shown = orm['dashboard.Video'].farmers_shown.through.objects.all()
        for i in range(0, dashboard_farmer_shown.count()/chunk + 1):
            dashboard_farmer_shown_slice = dashboard_farmer_shown[i*chunk:(i+1)*chunk]
            print "Farmers Shown Added %d" % (i*chunk)
            Farmer_Shown.objects.bulk_create([Farmer_Shown(person_id=orm['people.Person'].objects.get(old_coco_id=x.person_id).id, video_id=Video.objects.get(old_coco_id=x.video_id).id) for x in dashboard_farmer_shown_slice])

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'dashboard.animator': {
            'Meta': {'unique_together': "(('name', 'gender', 'partner', 'district'),)", 'object_name': 'Animator', 'db_table': "u'animator'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'ADDRESS'", 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'db_column': "'AGE'", 'blank': 'True'}),
            'assigned_villages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'assigned_villages'", 'to': u"orm['dashboard.Village']", 'through': u"orm['dashboard.AnimatorAssignedVillage']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'camera_operator_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'CAMERA_OPERATOR_FLAG'", 'blank': 'True'}),
            'csp_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'CSP_FLAG'", 'blank': 'True'}),
            'district': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.District']", 'null': 'True', 'blank': 'True'}),
            'facilitator_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'FACILITATOR_FLAG'", 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'GENDER'"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'NAME'"}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PHONE_NO'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'total_adoptions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_animator_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_animator_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']", 'null': 'True', 'db_column': "'home_village_id'", 'blank': 'True'})
        },
        u'dashboard.animatorassignedvillage': {
            'Meta': {'object_name': 'AnimatorAssignedVillage', 'db_table': "u'animator_assigned_village'"},
            'animator': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Animator']"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_animatorassignedvillage_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_animatorassignedvillage_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"})
        },
        u'dashboard.animatorsalarypermonth': {
            'Meta': {'object_name': 'AnimatorSalaryPerMonth', 'db_table': "u'animator_salary_per_month'"},
            'animator': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Animator']"}),
            'date': ('django.db.models.fields.DateField', [], {'db_column': "'DATE'"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'pay_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'PAY_DATE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'total_salary': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'TOTAL_SALARY'", 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_animatorsalarypermonth_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_animatorsalarypermonth_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.block': {
            'Meta': {'object_name': 'Block', 'db_table': "u'block'"},
            'block_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100', 'db_column': "'BLOCK_NAME'"}),
            'district': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.District']"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_block_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_block_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.cocouser': {
            'Meta': {'object_name': 'CocoUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_cocouser_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_cocouser_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'villages': ('dashboard.fields.related.BigManyToManyField', [], {'to': u"orm['dashboard.Village']", 'symmetrical': 'False'})
        },
        u'dashboard.country': {
            'Meta': {'object_name': 'Country', 'db_table': "u'country'"},
            'country_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100', 'db_column': "'COUNTRY_NAME'"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_country_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_country_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.developmentmanager': {
            'Meta': {'object_name': 'DevelopmentManager', 'db_table': "u'development_manager'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'ADDRESS'", 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'db_column': "'AGE'", 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'GENDER'"}),
            'hire_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'HIRE_DATE'", 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'NAME'"}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PHONE_NO'", 'blank': 'True'}),
            'region': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Region']"}),
            'salary': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'SALARY'", 'blank': 'True'}),
            'speciality': ('django.db.models.fields.TextField', [], {'db_column': "'SPECIALITY'", 'blank': 'True'}),
            'start_day': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DAY'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_developmentmanager_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_developmentmanager_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.district': {
            'Meta': {'object_name': 'District', 'db_table': "u'district'"},
            'district_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100', 'db_column': "'DISTRICT_NAME'"}),
            'fieldofficer': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.FieldOfficer']"}),
            'fieldofficer_startday': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'FIELDOFFICER_STARTDAY'", 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '31', 'decimal_places': '28', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '32', 'decimal_places': '28', 'blank': 'True'}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'state': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_district_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_district_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.equipment': {
            'Meta': {'object_name': 'Equipment', 'db_table': "u'equipment_id'"},
            'additional_accessories': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'COST'", 'blank': 'True'}),
            'equipment_type': ('django.db.models.fields.IntegerField', [], {'db_column': "'EQUIPMENT_TYPE'"}),
            'equipmentholder': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.EquipmentHolder']", 'null': 'True', 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'installation_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invoice_no': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "'INVOICE_NO'"}),
            'is_reserve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'model_no': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "'MODEL_NO'", 'blank': 'True'}),
            'other_equipment': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'db_column': "'OTHER_EQUIPMENT'", 'blank': 'True'}),
            'procurement_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'PROCUREMENT_DATE'", 'blank': 'True'}),
            'purpose': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'purpose'", 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'serial_no': ('django.db.models.fields.CharField', [], {'max_length': '300', 'db_column': "'SERIAL_NO'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'transfer_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_equipment_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_equipment_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']", 'null': 'True', 'blank': 'True'}),
            'warranty_expiration_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'WARRANTY_EXPIRATION_DATE'", 'blank': 'True'})
        },
        u'dashboard.equipmentholder': {
            'Meta': {'object_name': 'EquipmentHolder', 'db_table': "u'equipment_holder'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'object_id': ('dashboard.fields.fields.PositiveBigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_equipmentholder_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_equipmentholder_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.error': {
            'Meta': {'unique_together': "(('rule', 'content_type1', 'object_id1', 'content_type2', 'object_id2'),)", 'object_name': 'Error'},
            'content_type1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type1'", 'to': u"orm['contenttypes.ContentType']"}),
            'content_type2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_type2'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"}),
            'district': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.District']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notanerror': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'object_id1': ('dashboard.fields.fields.PositiveBigIntegerField', [], {}),
            'object_id2': ('dashboard.fields.fields.PositiveBigIntegerField', [], {'null': 'True'}),
            'rule': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['dashboard.Rule']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_error_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_error_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.fieldofficer': {
            'Meta': {'object_name': 'FieldOfficer', 'db_table': "u'field_officer'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'ADDRESS'", 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'db_column': "'AGE'", 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'GENDER'"}),
            'hire_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'HIRE_DATE'", 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'NAME'"}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PHONE_NO'", 'blank': 'True'}),
            'salary': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'SALARY'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_fieldofficer_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_fieldofficer_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.groupstargetedinscreening': {
            'Meta': {'object_name': 'GroupsTargetedInScreening', 'db_table': "u'screening_farmer_groups_targeted'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'persongroups': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.PersonGroups']", 'db_column': "'persongroups_id'"}),
            'screening': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Screening']", 'db_column': "'screening_id'"})
        },
        u'dashboard.language': {
            'Meta': {'object_name': 'Language', 'db_table': "u'language'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'language_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_language_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_language_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.monthlycostpervillage': {
            'Meta': {'object_name': 'MonthlyCostPerVillage', 'db_table': "u'monthly_cost_per_village'"},
            'community_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'COMMUNITY_COST'", 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'db_column': "'DATE'"}),
            'digitalgreen_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'DIGITALGREEN_COST'", 'blank': 'True'}),
            'equipment_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'EQUIPMENT_COST'", 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'labor_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'LABOR_COST'", 'blank': 'True'}),
            'miscellaneous_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'MISCELLANEOUS_COST'", 'blank': 'True'}),
            'partners_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'PARTNERS_COST'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'total_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'TOTAL_COST'", 'blank': 'True'}),
            'transportation_cost': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'TRANSPORTATION_COST'", 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_monthlycostpervillage_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_monthlycostpervillage_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"})
        },
        u'dashboard.offlineuser': {
            'Meta': {'object_name': 'OfflineUser'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'offline_pk_id': ('dashboard.fields.fields.PositiveBigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_offlineuser_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_offlineuser_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.partners': {
            'Meta': {'object_name': 'Partners', 'db_table': "u'partners'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'ADDRESS'", 'blank': 'True'}),
            'date_of_association': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'DATE_OF_ASSOCIATION'", 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'partner_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PARTNER_NAME'"}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PHONE_NO'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_partners_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_partners_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.person': {
            'Meta': {'unique_together': "(('person_name', 'father_name', 'village'),)", 'object_name': 'Person', 'db_table': "u'person'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'ADDRESS'", 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'db_column': "'AGE'", 'blank': 'True'}),
            'date_of_joining': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'FATHER_NAME'", 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'GENDER'"}),
            'group': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.PersonGroups']", 'null': 'True', 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'land_holdings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'db_column': "'LAND_HOLDINGS'", 'blank': 'True'}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PERSON_NAME'"}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'PHONE_NO'", 'blank': 'True'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'rel'", 'to': u"orm['dashboard.Person']", 'through': u"orm['dashboard.PersonRelations']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_person_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_person_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"})
        },
        u'dashboard.personadoptpractice': {
            'Meta': {'unique_together': "(('person', 'video', 'date_of_adoption'),)", 'object_name': 'PersonAdoptPractice', 'db_table': "u'person_adopt_practice'"},
            'date_of_adoption': ('django.db.models.fields.DateField', [], {'db_column': "'DATE_OF_ADOPTION'"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'person': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Person']"}),
            'prior_adoption_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'PRIOR_ADOPTION_FLAG'", 'blank': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'QUALITY'", 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'QUANTITY'", 'blank': 'True'}),
            'quantity_unit': ('django.db.models.fields.CharField', [], {'max_length': '150', 'db_column': "'QUANTITY_UNIT'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_personadoptpractice_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_personadoptpractice_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'video': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Video']"})
        },
        u'dashboard.persongroups': {
            'Meta': {'unique_together': "(('group_name', 'village'),)", 'object_name': 'PersonGroups', 'db_table': "u'person_groups'"},
            'days': ('django.db.models.fields.CharField', [], {'max_length': '9', 'db_column': "'DAYS'", 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'GROUP_NAME'"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_column': "'TIME_UPDATED'", 'blank': 'True'}),
            'timings': ('django.db.models.fields.TimeField', [], {'null': 'True', 'db_column': "'TIMINGS'", 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_persongroups_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_persongroups_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"})
        },
        u'dashboard.personmeetingattendance': {
            'Meta': {'object_name': 'PersonMeetingAttendance', 'db_table': "u'person_meeting_attendance'"},
            'expressed_adoption_video': ('dashboard.fields.related.BigForeignKey', [], {'blank': 'True', 'related_name': "'expressed_adoption_video'", 'null': 'True', 'db_column': "'EXPRESSED_ADOPTION_VIDEO'", 'to': u"orm['dashboard.Video']"}),
            'expressed_question': ('django.db.models.fields.CharField', [], {'max_length': '500', 'db_column': "'EXPRESSED_QUESTION'", 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'interested': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'INTERESTED'", 'db_index': 'True'}),
            'person': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Person']"}),
            'screening': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Screening']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_personmeetingattendance_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_personmeetingattendance_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.personrelations': {
            'Meta': {'object_name': 'PersonRelations', 'db_table': "u'person_relations'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'person': ('dashboard.fields.related.BigForeignKey', [], {'related_name': "'person'", 'to': u"orm['dashboard.Person']"}),
            'relative': ('dashboard.fields.related.BigForeignKey', [], {'related_name': "'relative'", 'to': u"orm['dashboard.Person']"}),
            'type_of_relationship': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'TYPE_OF_RELATIONSHIP'"})
        },
        u'dashboard.personshowninvideo': {
            'Meta': {'object_name': 'PersonShownInVideo', 'db_table': "u'video_farmers_shown'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'person': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Person']", 'db_column': "'person_id'"}),
            'video': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Video']", 'db_column': "'video_id'"})
        },
        u'dashboard.practices': {
            'Meta': {'unique_together': "(('practice_sector', 'practice_subsector', 'practice_topic', 'practice_subtopic', 'practice_subject'),)", 'object_name': 'Practices', 'db_table': "u'practices'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'practice_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'db_column': "'PRACTICE_NAME'"}),
            'practice_sector': ('dashboard.fields.related.BigForeignKey', [], {'default': '1', 'to': u"orm['dashboard.PracticeSector']"}),
            'practice_subject': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.PracticeSubject']", 'null': 'True', 'blank': 'True'}),
            'practice_subsector': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.PracticeSubSector']", 'null': 'True', 'blank': 'True'}),
            'practice_subtopic': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.PracticeSubtopic']", 'null': 'True', 'blank': 'True'}),
            'practice_topic': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.PracticeTopic']", 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practices_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practices_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.practicesector': {
            'Meta': {'object_name': 'PracticeSector', 'db_table': "u'practice_sector'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesector_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesector_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.practicesubject': {
            'Meta': {'object_name': 'PracticeSubject', 'db_table': "u'practice_subject'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesubject_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesubject_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.practicesubsector': {
            'Meta': {'object_name': 'PracticeSubSector', 'db_table': "u'practice_subsector'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesubsector_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesubsector_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.practicesubtopic': {
            'Meta': {'object_name': 'PracticeSubtopic', 'db_table': "u'practice_subtopic'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesubtopic_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicesubtopic_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.practicetopic': {
            'Meta': {'object_name': 'PracticeTopic', 'db_table': "u'practice_topic'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicetopic_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_practicetopic_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.region': {
            'Meta': {'object_name': 'Region', 'db_table': "u'region'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100', 'db_column': "'REGION_NAME'"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_region_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_region_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.regiontest': {
            'Meta': {'object_name': 'RegionTest', 'db_table': "u'region_test'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'id'"}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100', 'db_column': "'REGION_NAME'"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_regiontest_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_regiontest_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.reviewer': {
            'Meta': {'object_name': 'Reviewer', 'db_table': "u'reviewer'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'object_id': ('dashboard.fields.fields.PositiveBigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_reviewer_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_reviewer_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.rule': {
            'Meta': {'object_name': 'Rule'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'error_msg': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_rule_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_rule_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.screening': {
            'Meta': {'unique_together': "(('date', 'start_time', 'end_time', 'animator', 'village'),)", 'object_name': 'Screening', 'db_table': "u'screening'"},
            'animator': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Animator']"}),
            'date': ('django.db.models.fields.DateField', [], {'db_column': "'DATE'"}),
            'end_time': ('django.db.models.fields.TimeField', [], {'db_column': "'END_TIME'"}),
            'farmer_groups_targeted': ('dashboard.fields.related.BigManyToManyField', [], {'to': u"orm['dashboard.PersonGroups']", 'symmetrical': 'False'}),
            'farmers_attendance': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['dashboard.Person']", 'null': "'False'", 'through': u"orm['dashboard.PersonMeetingAttendance']", 'blank': "'False'"}),
            'fieldofficer': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.FieldOfficer']", 'null': 'True', 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'LOCATION'", 'blank': 'True'}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'start_time': ('django.db.models.fields.TimeField', [], {'db_column': "'START_TIME'"}),
            'target_adoptions': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'TARGET_ADOPTIONS'", 'blank': 'True'}),
            'target_audience_interest': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'TARGET_AUDIENCE_INTEREST'", 'blank': 'True'}),
            'target_person_attendance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'TARGET_PERSON_ATTENDANCE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_screening_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_screening_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'videoes_screened': ('dashboard.fields.related.BigManyToManyField', [], {'to': u"orm['dashboard.Video']", 'symmetrical': 'False'}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"})
        },
        u'dashboard.serverlog': {
            'Meta': {'object_name': 'ServerLog'},
            'action': ('django.db.models.fields.IntegerField', [], {}),
            'entry_table': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'partner': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'village': ('django.db.models.fields.BigIntegerField', [], {'null': 'True'})
        },
        u'dashboard.state': {
            'Meta': {'object_name': 'State', 'db_table': "u'state'"},
            'country': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Country']"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'region': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Region']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100', 'db_column': "'STATE_NAME'"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_state_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_state_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'dashboard.target': {
            'Meta': {'unique_together': "(('district', 'month_year'),)", 'object_name': 'Target'},
            'adoption_per_dissemination': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'avg_attendance_per_dissemination': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'challenges': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'clusters_identification': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crp_refresher_training': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'crp_training': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'csp_identification': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'csp_refresher_training': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'csp_training': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dg_concept_sharing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'dissemination_set_deployment': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'disseminations': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.District']"}),
            'editor_refresher_training': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'editor_training': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'exp_interest_per_dissemination': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'month_year': ('django.db.models.fields.DateField', [], {}),
            'storyboard_preparation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'support_requested': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_target_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_target_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'video_editing': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'video_production': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'video_quality_checking': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'video_shooting': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'video_uploading': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'village_operationalization': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'villages_certification': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'what_not_went_well': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'what_went_well': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'dashboard.training': {
            'Meta': {'unique_together': "(('training_start_date', 'training_end_date', 'village'),)", 'object_name': 'Training', 'db_table': "u'training'"},
            'animators_trained': ('dashboard.fields.related.BigManyToManyField', [], {'to': u"orm['dashboard.Animator']", 'symmetrical': 'False'}),
            'development_manager_present': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.DevelopmentManager']", 'null': 'True', 'db_column': "'dm_id'", 'blank': 'True'}),
            'fieldofficer': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.FieldOfficer']", 'db_column': "'fieldofficer_id'"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'training_end_date': ('django.db.models.fields.DateField', [], {'db_column': "'TRAINING_END_DATE'"}),
            'training_outcome': ('django.db.models.fields.TextField', [], {'db_column': "'TRAINING_OUTCOME'", 'blank': 'True'}),
            'training_purpose': ('django.db.models.fields.TextField', [], {'db_column': "'TRAINING_PURPOSE'", 'blank': 'True'}),
            'training_start_date': ('django.db.models.fields.DateField', [], {'db_column': "'TRAINING_START_DATE'"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_training_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_training_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"})
        },
        u'dashboard.traininganimatorstrained': {
            'Meta': {'object_name': 'TrainingAnimatorsTrained', 'db_table': "u'training_animators_trained'"},
            'animator': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Animator']", 'db_column': "'animator_id'"}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'training': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Training']", 'db_column': "'training_id'"})
        },
        u'dashboard.userpermission': {
            'Meta': {'object_name': 'UserPermission'},
            'district_operated': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.District']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region_operated': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Region']", 'null': 'True', 'blank': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_userpermission_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_userpermission_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'username': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'dashboard.video': {
            'Meta': {'unique_together': "(('title', 'video_production_start_date', 'video_production_end_date', 'village'),)", 'object_name': 'Video', 'db_table': "u'video'"},
            'actors': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'ACTORS'"}),
            'approval_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'APPROVAL_DATE'", 'blank': 'True'}),
            'audio_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'AUDIO_QUALITY'", 'blank': 'True'}),
            'cameraoperator': ('dashboard.fields.related.BigForeignKey', [], {'related_name': "'cameraoperator'", 'to': u"orm['dashboard.Animator']"}),
            'duration': ('django.db.models.fields.TimeField', [], {'null': 'True', 'db_column': "'DURATION'", 'blank': 'True'}),
            'edit_finish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'EDIT_FINISH_DATE'", 'blank': 'True'}),
            'edit_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'EDIT_START_DATE'", 'blank': 'True'}),
            'editing_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'EDITING_QUALITY'", 'blank': 'True'}),
            'facilitator': ('dashboard.fields.related.BigForeignKey', [], {'related_name': "'facilitator'", 'to': u"orm['dashboard.Animator']"}),
            'farmers_shown': ('dashboard.fields.related.BigManyToManyField', [], {'to': u"orm['dashboard.Person']", 'symmetrical': 'False'}),
            'final_edited_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'db_column': "'FINAL_EDITED_FILENAME'", 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'language': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Language']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'movie_maker_project_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'db_column': "'MOVIE_MAKER_PROJECT_FILENAME'", 'blank': 'True'}),
            'partner': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Partners']"}),
            'picture_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'PICTURE_QUALITY'", 'blank': 'True'}),
            'raw_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'db_column': "'RAW_FILENAME'", 'blank': 'True'}),
            'related_practice': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Practices']", 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'db_column': "'REMARKS'", 'blank': 'True'}),
            'reviewer': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Reviewer']", 'null': 'True', 'blank': 'True'}),
            'storybase': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'db_column': "'STORYBASE'", 'blank': 'True'}),
            'storyboard_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'db_column': "'STORYBOARD_FILENAME'", 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'db_column': "'SUMMARY'", 'blank': 'True'}),
            'supplementary_video_produced': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Video']", 'null': 'True', 'blank': 'True'}),
            'thematic_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'THEMATIC_QUALITY'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_column': "'TITLE'"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_video_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_video_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'video_production_end_date': ('django.db.models.fields.DateField', [], {'db_column': "'VIDEO_PRODUCTION_END_DATE'"}),
            'video_production_start_date': ('django.db.models.fields.DateField', [], {'db_column': "'VIDEO_PRODUCTION_START_DATE'"}),
            'video_suitable_for': ('django.db.models.fields.IntegerField', [], {'db_column': "'VIDEO_SUITABLE_FOR'"}),
            'video_type': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'db_column': "'VIDEO_TYPE'"}),
            'viewers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"}),
            'youtubeid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_column': "'YOUTUBEID'", 'blank': 'True'})
        },
        u'dashboard.videosscreenedinscreening': {
            'Meta': {'object_name': 'VideosScreenedInScreening', 'db_table': "u'screening_videoes_screened'"},
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'screening': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Screening']", 'db_column': "'screening_id'"}),
            'video': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Video']", 'db_column': "'video_id'"})
        },
        u'dashboard.village': {
            'Meta': {'unique_together': "(('village_name', 'block'),)", 'object_name': 'Village', 'db_table': "u'village'"},
            'block': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Block']"}),
            'control': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'db_column': "'CONTROL'", 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('dashboard.fields.fields.BigAutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'no_of_households': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'NO_OF_HOUSEHOLDS'", 'blank': 'True'}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'POPULATION'", 'blank': 'True'}),
            'road_connectivity': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'ROAD_CONNECTIVITY'", 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'db_column': "'START_DATE'", 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_village_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_village_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_column': "'VILLAGE_NAME'"})
        },
        u'dashboard.villageprecalculation': {
            'Meta': {'unique_together': "(('village', 'date'),)", 'object_name': 'VillagePrecalculation', 'db_table': "u'village_precalculation'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'total_active_attendees': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'total_adopted_attendees': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'total_adoption_by_active': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_villageprecalculation_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'dashboard_villageprecalculation_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('dashboard.fields.related.BigForeignKey', [], {'to': u"orm['dashboard.Village']"})
        },
        u'geographies.block': {
            'Meta': {'object_name': 'Block'},
            'block_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_block_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_block_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.country': {
            'Meta': {'object_name': 'Country'},
            'country_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_country_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_country_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.district': {
            'Meta': {'object_name': 'District'},
            'district_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '31', 'decimal_places': '28', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '32', 'decimal_places': '28', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.State']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_district_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_district_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.region': {
            'Meta': {'object_name': 'Region'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'region_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_region_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_region_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.state': {
            'Meta': {'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Region']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'state_name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_state_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_state_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'geographies.village': {
            'Meta': {'unique_together': "(('village_name', 'block'),)", 'object_name': 'Village'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Block']"}),
            'control': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'no_of_households': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'population': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'road_connectivity': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_village_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'geographies_village_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village_name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'people.animator': {
            'Meta': {'unique_together': "(('name', 'gender', 'partner', 'district'),)", 'object_name': 'Animator'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'assigned_villages': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'assigned_villages'", 'to': u"orm['geographies.Village']", 'through': u"orm['people.AnimatorAssignedVillage']", 'blank': 'True', 'symmetrical': 'False', 'null': 'True'}),
            'camera_operator_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'csp_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.District']", 'null': 'True', 'blank': 'True'}),
            'facilitator_flag': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'total_adoptions': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animator_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animator_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']", 'null': 'True', 'blank': 'True'})
        },
        u'people.animatorassignedvillage': {
            'Meta': {'object_name': 'AnimatorAssignedVillage'},
            'animator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.Animator']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animatorassignedvillage_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_animatorassignedvillage_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
        u'people.person': {
            'Meta': {'unique_together': "(('person_name', 'father_name', 'village'),)", 'object_name': 'Person'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'age': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'date_of_joining': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['people.PersonGroup']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_exists': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'land_holdings': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_person_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_person_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
        u'people.persongroup': {
            'Meta': {'unique_together': "(('group_name', 'village'),)", 'object_name': 'PersonGroup'},
            'days': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'timings': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_persongroup_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'people_persongroup_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"})
        },
        u'programs.partner': {
            'Meta': {'object_name': 'Partner'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'date_of_association': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {'db_index': 'True'}),
            'partner_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'programs_partner_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'programs_partner_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.language': {
            'Meta': {'object_name': 'Language'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': "'True'", 'max_length': '100'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_language_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_language_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practice': {
            'Meta': {'unique_together': "(('practice_sector', 'practice_subsector', 'practice_topic', 'practice_subtopic', 'practice_subject'),)", 'object_name': 'Practice'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'practice_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'practice_sector': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['videos.PracticeSector']"}),
            'practice_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeSubject']", 'null': 'True', 'blank': 'True'}),
            'practice_subsector': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeSubSector']", 'null': 'True', 'blank': 'True'}),
            'practice_subtopic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeSubtopic']", 'null': 'True', 'blank': 'True'}),
            'practice_topic': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.PracticeTopic']", 'null': 'True', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practice_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practice_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesector': {
            'Meta': {'object_name': 'PracticeSector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesector_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesector_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesubject': {
            'Meta': {'object_name': 'PracticeSubject'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubject_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubject_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesubsector': {
            'Meta': {'object_name': 'PracticeSubSector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubsector_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubsector_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicesubtopic': {
            'Meta': {'object_name': 'PracticeSubtopic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubtopic_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicesubtopic_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.practicetopic': {
            'Meta': {'object_name': 'PracticeTopic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicetopic_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_practicetopic_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'videos.video': {
            'Meta': {'unique_together': "(('title', 'video_production_start_date', 'video_production_end_date', 'village'),)", 'object_name': 'Video'},
            'actors': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'approval_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'audio_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'cameraoperator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cameraoperator'", 'to': u"orm['people.Animator']"}),
            'duration': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'edit_finish_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'edit_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'editing_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'facilitator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'facilitator'", 'to': u"orm['people.Animator']"}),
            'farmers_shown': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['people.Person']", 'symmetrical': 'False'}),
            'final_edited_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Language']"}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'movie_maker_project_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'old_coco_id': ('django.db.models.fields.BigIntegerField', [], {}),
            'partner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['programs.Partner']"}),
            'picture_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'raw_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'related_practice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Practice']", 'null': 'True', 'blank': 'True'}),
            'remarks': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'storybase': ('django.db.models.fields.IntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'storyboard_filename': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'supplementary_video_produced': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['videos.Video']", 'null': 'True', 'blank': 'True'}),
            'thematic_quality': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_video_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'videos_video_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'video_production_end_date': ('django.db.models.fields.DateField', [], {}),
            'video_production_start_date': ('django.db.models.fields.DateField', [], {}),
            'video_suitable_for': ('django.db.models.fields.IntegerField', [], {}),
            'video_type': ('django.db.models.fields.IntegerField', [], {'max_length': '1'}),
            'viewers': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['geographies.Village']"}),
            'youtubeid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        }
    }

    complete_apps = ['dashboard', 'videos']
    symmetrical = True