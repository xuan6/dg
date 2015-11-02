# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'IvrSubscriber'
        db.create_table(u'ivr_ivrsubscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=13)),
        ))
        db.send_create_signal(u'ivr', ['IvrSubscriber'])

        # Adding M2M table for field subscribed_channels on 'IvrSubscriber'
        db.create_table(u'ivr_ivrsubscriber_subscribed_channels', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ivrsubscriber', models.ForeignKey(orm[u'ivr.ivrsubscriber'], null=False)),
            ('channel', models.ForeignKey(orm[u'ivr.channel'], null=False))
        ))
        db.create_unique(u'ivr_ivrsubscriber_subscribed_channels', ['ivrsubscriber_id', 'channel_id'])

        # Adding model 'Channel'
        db.create_table(u'ivr_channel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'ivr', ['Channel'])

        # Adding model 'UsaidData'
        db.create_table(u'ivr_usaiddata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('video', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('touchtone_response', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('phone_no', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ivr', ['UsaidData'])

        # Removing M2M table for field district on 'Broadcast'
        db.delete_table('ivr_broadcast_district')

        # Adding M2M table for field channels on 'Broadcast'
        db.create_table(u'ivr_broadcast_channels', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('broadcast', models.ForeignKey(orm[u'ivr.broadcast'], null=False)),
            ('channel', models.ForeignKey(orm[u'ivr.channel'], null=False))
        ))
        db.create_unique(u'ivr_broadcast_channels', ['broadcast_id', 'channel_id'])

        # Deleting field 'Audio.meta'
        db.delete_column(u'ivr_audio', 'meta')

        # Adding M2M table for field channels on 'Audio'
        db.create_table(u'ivr_audio_channels', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('audio', models.ForeignKey(orm[u'ivr.audio'], null=False)),
            ('channel', models.ForeignKey(orm[u'ivr.channel'], null=False))
        ))
        db.create_unique(u'ivr_audio_channels', ['audio_id', 'channel_id'])


    def backwards(self, orm):
        # Deleting model 'IvrSubscriber'
        db.delete_table(u'ivr_ivrsubscriber')

        # Removing M2M table for field subscribed_channels on 'IvrSubscriber'
        db.delete_table('ivr_ivrsubscriber_subscribed_channels')

        # Deleting model 'Channel'
        db.delete_table(u'ivr_channel')

        # Deleting model 'UsaidData'
        db.delete_table(u'ivr_usaiddata')

        # Adding M2M table for field district on 'Broadcast'
        db.create_table(u'ivr_broadcast_district', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('broadcast', models.ForeignKey(orm[u'ivr.broadcast'], null=False)),
            ('district', models.ForeignKey(orm[u'geographies.district'], null=False))
        ))
        db.create_unique(u'ivr_broadcast_district', ['broadcast_id', 'district_id'])

        # Removing M2M table for field channels on 'Broadcast'
        db.delete_table('ivr_broadcast_channels')

        # Adding field 'Audio.meta'
        db.add_column(u'ivr_audio', 'meta',
                      self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field channels on 'Audio'
        db.delete_table('ivr_audio_channels')


    models = {
        u'ivr.audio': {
            'Meta': {'object_name': 'Audio'},
            'audio_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'audio_status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'channels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ivr.Channel']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ivr.broadcast': {
            'Meta': {'object_name': 'Broadcast'},
            'audio_file': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ivr.Audio']"}),
            'channels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ivr.Channel']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'schedule_call': ('django.db.models.fields.DateTimeField', [], {}),
            'service': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'ivr.call': {
            'Meta': {'object_name': 'Call'},
            'attributes': ('django.db.models.fields.TextField', [], {'max_length': '5000'}),
            'exotel_call_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'time_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'ivr.channel': {
            'Meta': {'object_name': 'Channel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'ivr.ivrsubscriber': {
            'Meta': {'object_name': 'IvrSubscriber'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'subscribed_channels': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['ivr.Channel']", 'symmetrical': 'False'})
        },
        u'ivr.usaiddata': {
            'Meta': {'object_name': 'UsaidData'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_no': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'touchtone_response': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'video': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ivr']