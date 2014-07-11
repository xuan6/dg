# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExampleVillage'
        db.create_table(u'exampleapp_examplevillage', (
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='examplevillage_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='examplevillage_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='id')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('block_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('district_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('state_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'exampleapp', ['ExampleVillage'])

        # Adding model 'ExampleGroup'
        db.create_table(u'exampleapp_examplegroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='id')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exampleapp.ExampleVillage'])),
        ))
        db.send_create_signal(u'exampleapp', ['ExampleGroup'])

        # Adding model 'ExamplePerson'
        db.create_table(u'exampleapp_exampleperson', (
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='exampleperson_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='exampleperson_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True, db_column='id')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('village', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exampleapp.ExampleVillage'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exampleapp.ExampleGroup'])),
        ))
        db.send_create_signal(u'exampleapp', ['ExamplePerson'])

        # Adding model 'ExampleUser'
        db.create_table(u'exampleapp_exampleuser', (
            ('user_created', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'exampleapp_exampleuser_created', null=True, to=orm['auth.User'])),
            ('time_created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'exampleapp_exampleuser_related_modified', null=True, to=orm['auth.User'])),
            ('time_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, null=True, blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='exampleapp_user', unique=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'exampleapp', ['ExampleUser'])

        # Adding M2M table for field villages on 'ExampleUser'
        db.create_table(u'exampleapp_exampleuser_villages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exampleuser', models.ForeignKey(orm[u'exampleapp.exampleuser'], null=False)),
            ('examplevillage', models.ForeignKey(orm[u'exampleapp.examplevillage'], null=False))
        ))
        db.create_unique(u'exampleapp_exampleuser_villages', ['exampleuser_id', 'examplevillage_id'])

        # Adding model 'FullDownloadStats'
        db.create_table(u'exampleapp_fulldownloadstats', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exampleapp.ExampleUser'])),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'exampleapp', ['FullDownloadStats'])

        # Adding model 'ServerLog'
        db.create_table(u'exampleapp_serverlog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.utcnow)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='serverlog_user', null=True, to=orm['exampleapp.ExampleUser'])),
            ('village', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('action', self.gf('django.db.models.fields.IntegerField')()),
            ('entry_table', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('model_id', self.gf('django.db.models.fields.IntegerField')(null=True)),
        ))
        db.send_create_signal(u'exampleapp', ['ServerLog'])


    def backwards(self, orm):
        # Deleting model 'ExampleVillage'
        db.delete_table(u'exampleapp_examplevillage')

        # Deleting model 'ExampleGroup'
        db.delete_table(u'exampleapp_examplegroup')

        # Deleting model 'ExamplePerson'
        db.delete_table(u'exampleapp_exampleperson')

        # Deleting model 'ExampleUser'
        db.delete_table(u'exampleapp_exampleuser')

        # Removing M2M table for field villages on 'ExampleUser'
        db.delete_table('exampleapp_exampleuser_villages')

        # Deleting model 'FullDownloadStats'
        db.delete_table(u'exampleapp_fulldownloadstats')

        # Deleting model 'ServerLog'
        db.delete_table(u'exampleapp_serverlog')


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
        u'exampleapp.examplegroup': {
            'Meta': {'object_name': 'ExampleGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'id'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exampleapp.ExampleVillage']"})
        },
        u'exampleapp.exampleperson': {
            'Meta': {'object_name': 'ExamplePerson'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exampleapp.ExampleGroup']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'id'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'exampleperson_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'exampleperson_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'village': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exampleapp.ExampleVillage']"})
        },
        u'exampleapp.exampleuser': {
            'Meta': {'object_name': 'ExampleUser'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'exampleapp_user'", 'unique': 'True', 'to': u"orm['auth.User']"}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'exampleapp_exampleuser_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'exampleapp_exampleuser_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'villages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['exampleapp.ExampleVillage']", 'symmetrical': 'False'})
        },
        u'exampleapp.examplevillage': {
            'Meta': {'object_name': 'ExampleVillage'},
            'block_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'district_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True', 'db_column': "'id'"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'state_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'time_created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'time_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'examplevillage_created'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'user_modified': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'examplevillage_related_modified'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'exampleapp.fulldownloadstats': {
            'Meta': {'object_name': 'FullDownloadStats'},
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exampleapp.ExampleUser']"})
        },
        u'exampleapp.serverlog': {
            'Meta': {'object_name': 'ServerLog'},
            'action': ('django.db.models.fields.IntegerField', [], {}),
            'entry_table': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_id': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.utcnow'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'serverlog_user'", 'null': 'True', 'to': u"orm['exampleapp.ExampleUser']"}),
            'village': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['exampleapp']